# Proyecto GEIH 2025

Estructura base para trabajar el proyecto en Visual Studio Code con Python y Jupyter Notebook.

## Entorno virtual Python

Ejecutar:

python -m venv env

Activar entorno virtual:

env\Scripts\activate

Luego de creado y activado el entorno virtual ejecutar:

pip install -r requirements.txt

## Orden sugerido de ejecución

1. `notebooks/01_revision_archivos.ipynb`
2. `notebooks/02_consolidacion_modulos_2025.ipynb`
3. `notebooks/03_limpieza_y_base_analitica.ipynb`
4. `notebooks/04_eda_avance_1.ipynb`

## Estructura

- `src/utils.py`: funciones auxiliares reutilizables.
- `src/config.py`: rutas y configuración general.
- `notebooks/`: notebooks del flujo del proyecto.
- `outputs/`: tablas y gráficos exportados.
- `data_processed/`: salidas intermedias y base analítica.

## Documento en construcción

- `documento\avance1_primera_versión_geih_2025.docx`: Documento del primer avance del proyecto integrador.
