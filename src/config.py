from pathlib import Path

PROJECT_ROOT = Path.cwd().resolve().parent if Path.cwd().name == 'notebooks' else Path.cwd().resolve()
DATA_RAW = PROJECT_ROOT / 'data_raw'
DATA_PROCESSED = PROJECT_ROOT / 'data_processed'
ANNUAL_MODULES = DATA_PROCESSED / 'annual_modules'
ANALYTIC_BASE = DATA_PROCESSED / 'analytic_base'
DICTIONARIES = DATA_PROCESSED / 'dictionaries'
OUTPUTS = PROJECT_ROOT / 'outputs'
TABLES = OUTPUTS / 'tablas'
FIGURES = OUTPUTS / 'graficos'
NOTEBOOKS = PROJECT_ROOT / 'notebooks'

EXPECTED_MONTHS = [f'2025_{i:02d}' for i in range(1, 13)]
EXPECTED_MODULES = {
    'caracteristicas': ['Caracteristicas', 'Características'],
    'fuerza_trabajo': ['Fuerza'],
    'ocupados': ['Ocupados'],
    'no_ocupados': ['No-ocupados', 'No ocupados'],
    'hogar_vivienda': ['Datos-del-hogar', 'Datos del hogar'],
    'migracion': ['Migracion', 'Migración'],
    'otras_formas_trabajo': ['Otras-formas', 'Otras formas'],
    'otros_ingresos': ['Otros-ingresos', 'Otros ingresos']
}

KEY_COLUMNS = ['DIRECTORIO', 'SECUENCIAP', 'ORDEN', 'HOGAR', 'REGIS']
