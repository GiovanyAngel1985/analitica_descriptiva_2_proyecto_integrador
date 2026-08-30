from pathlib import Path
import pandas as pd


def listar_carpetas_mensuales(data_raw):
    return sorted([p for p in Path(data_raw).iterdir() if p.is_dir() and p.name.startswith('2025_')])


def inventario_archivos(data_raw):
    registros = []
    for carpeta in listar_carpetas_mensuales(data_raw):
        for archivo in carpeta.iterdir():
            if archivo.is_file():
                registros.append({
                    'mes': carpeta.name,
                    'archivo': archivo.name,
                    'ruta': str(archivo)
                })
    return pd.DataFrame(registros)


def buscar_archivo_por_patrones(carpeta, patrones):
    archivos = [p for p in Path(carpeta).iterdir() if p.is_file()]
    for archivo in archivos:
        nombre = archivo.name.lower()
        if all(p.lower() not in nombre for p in []):
            pass
        for patron in patrones:
            if patron.lower() in nombre:
                return archivo
    return None


def detectar_separador(file_path, encoding='latin-1', n=5):
    candidatos = [',', ';', '\t', '|']
    resultados = {}
    for sep in candidatos:
        try:
            df = pd.read_csv(file_path, sep=sep, encoding=encoding, nrows=n, low_memory=False)
            resultados[sep] = df.shape[1]
        except Exception:
            resultados[sep] = 0
    return max(resultados, key=resultados.get)

def leer_csv_seguro(file_path, sep=None, nrows=None):
    file_path = Path(file_path)
    encodings = ['utf-8', 'latin-1', 'cp1252']
    ultimo_error = None

    for encoding in encodings:
        try:
            if sep is None:
                sep_detectado = detectar_separador(file_path, encoding=encoding)
            else:
                sep_detectado = sep

            df = pd.read_csv(
                file_path,
                sep=sep_detectado,
                encoding=encoding,
                nrows=nrows,
                low_memory=False
            )
            print(f'Leído correctamente: {file_path.name} | encoding={encoding} | sep={sep_detectado}')
            return df
        except Exception as e:
            ultimo_error = e

    raise ultimo_error


def estandarizar_columnas(df):
    df = df.copy()
    df.columns = [c.strip().upper().replace(' ', '_') for c in df.columns]
    return df


def resumen_faltantes(df):
    faltantes = df.isna().sum().reset_index()
    faltantes.columns = ['variable', 'n_faltantes']
    faltantes['pct_faltantes'] = faltantes['n_faltantes'] / len(df)
    return faltantes.sort_values('pct_faltantes', ascending=False)


def validar_llaves(df, keys):
    df = df.copy()
    disponibles = [k for k in keys if k in df.columns]
    if not disponibles:
        return {'llaves_disponibles': [], 'duplicados': None}
    duplicados = df.duplicated(subset=disponibles).sum()
    return {'llaves_disponibles': disponibles, 'duplicados': int(duplicados)}


def exportar_csv(df, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def tabla_descriptiva(df, variables):
    desc = df[variables].describe().T
    desc['mediana'] = df[variables].median()
    desc['asimetria'] = df[variables].skew(numeric_only=True)
    columnas = ['count', 'mean', 'mediana', 'std', 'min', '25%', '50%', '75%', 'max', 'asimetria']
    return desc[columnas]
