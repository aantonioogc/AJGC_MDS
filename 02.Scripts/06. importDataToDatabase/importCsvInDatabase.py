import subprocess
import pandas as pd

# Lista de archivos CSV correspondientes a cada tabla
csv_files = [
    "yelp_academic_dataset_business_transformed.csv",
    "yelp_academic_dataset_checkin_transformed.csv",
    "yelp_academic_dataset_review_transformed.csv",
    "yelp_academic_dataset_tip_transformed.csv",
    "yelp_academic_dataset_user_transformed.csv"
]

# Función para obtener el tipo de datos de una columna del DataFrame
def get_data_type(column):
    data_type = "STRING"
    if column.dtype == "int64":
        data_type = "INTEGER"
    elif column.dtype == "float64":
        data_type = "FLOAT"
    return data_type

# Función para crear tabla y cargar datos
def create_table_and_load_data(csv_file):
    # Nombre de la tabla basado en el nombre del archivo CSV
    table_name = csv_file.replace("_transformed.csv", "").replace("yelp_academic_dataset_", "") + "_csv"

    # Leer datos del archivo CSV
    df = pd.read_csv(csv_file)

    # Obtener tipos de datos para cada columna
    column_types = {column: get_data_type(df[column]) for column in df.columns}

    # Comando para crear la tabla en CrateDB
    create_table_command = f"docker exec -i cratedb /usr/local/bin/crash -c \"CREATE TABLE IF NOT EXISTS {table_name} (" \
                       f"    {', '.join([f'{column} {column_types[column]}' for column in df.columns])}" \
                       f");\""

    # Ejecutar comando para crear la tabla
    subprocess.run(create_table_command, shell=True)

    # Ruta al archivo CSV dentro del contenedor de CrateDB
    container_csv_path = f"/dataset/{csv_file}"

    # Comando para importar datos desde el archivo CSV a CrateDB
    import_data_command = f"docker exec -i cratedb /usr/local/bin/crash -c \"COPY {table_name} FROM '{container_csv_path}' WITH (format = 'csv');\""

    # Ejecutar comando para importar datos
    subprocess.run(import_data_command, shell=True)

    print(f"Data from '{csv_file}' has been successfully imported to table '{table_name}' in CrateDB.")

# Procesar cada archivo CSV
for csv_file in csv_files:
    create_table_and_load_data(csv_file)
