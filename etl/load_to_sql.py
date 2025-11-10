import os
import pandas as pd
import pyodbc
from dotenv import load_dotenv


load_dotenv()

SQL_SERVER = os.getenv("SQL_SERVER")
SQL_DATABASE = os.getenv("SQL_DATABASE")
SQL_USERNAME = os.getenv("SQL_USERNAME")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")
CLEAN_CSV_PATH = "data_clean/dim_order.csv"



print("Leyendo archivo limpio...")
df = pd.read_csv(CLEAN_CSV_PATH)
print(f"Archivo cargado: {len(df)} filas\n")



print("Conectando a Azure SQL Database...")

connection_string = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    f"SERVER={SQL_SERVER};"
    f"DATABASE={SQL_DATABASE};"
    f"UID={SQL_USERNAME};"
    f"PWD={SQL_PASSWORD};"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)


try:
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    print("Conexión exitosa a Azure SQL\n")
except Exception as e:
    print("Error conectando a Azure SQL")
    print(e)
    exit()



print("Insertando datos en la tabla ...")

# insert_query = """
#     INSERT INTO superstore_clean (
#         row_id, order_id, order_date, ship_date, ship_mode, customer_id,
#         customer_name, segment, country, city, state, postal_code, region,
#         product_id, category, sub_category, product_name, sales, quantity,
#         discount, profit, delivery_days, profit_ratio, order_year, order_month
#     )
#     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
# """

insert_query = """
    INSERT INTO dim_order (
        order_key,
        order_id,
        order_date_key,
        ship_date_key
    )
    VALUES (?, ?, ?, ?)
"""


try:
    for row in df.itertuples(index=False):
        cursor.execute(insert_query, *row)

    conn.commit()
    print("Datos cargados correctamente en Azure SQL Database")

except Exception as e:
    print("Error insertando datos:")
    print(e)

finally:
    cursor.close()
    conn.close()
    print("Conexión cerrada")
