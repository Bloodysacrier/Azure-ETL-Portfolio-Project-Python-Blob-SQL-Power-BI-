import kagglehub
import pandas as pd

path = kagglehub.dataset_download("vivek468/superstore-dataset-final")

df = pd.read_csv(path + "/Sample - Superstore.csv", encoding="latin1")
df.to_csv("data_raw/raw_superstore.csv", index=False)
# ========================
# 1. Normalizar nombres de columnas
# ========================
df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]

# ========================
# 2. Convertir fechas
# ========================
df["order_date"] = pd.to_datetime(df["order_date"])
df["ship_date"] = pd.to_datetime(df["ship_date"])

# ========================
# 3. Crear nuevas columnas 
# ========================

# Días para entregar
df["delivery_days"] = (df["ship_date"] - df["order_date"]).dt.days

# Margen relativo
df["profit_ratio"] = df["profit"] / df["sales"]

# Año, Mes
df["order_year"] = df["order_date"].dt.year
df["order_month"] = df["order_date"].dt.month

# ========================
# 4. Eliminar duplicados
# ========================
df = df.drop_duplicates()

# ========================
# 5. Manejo de valores nulos
# ========================
df = df.fillna({
    "profit_ratio": 0,
    "delivery_days": df["delivery_days"].median()
})


# Extraer solo columnas necesarias de la tabla original
orders = df[["order_id", "order_date", "ship_date"]].drop_duplicates()

# Crear claves de fechas 
orders["order_date_key"] = orders["order_date"].dt.strftime("%Y%m%d").astype(int)
orders["ship_date_key"] = orders["ship_date"].dt.strftime("%Y%m%d").astype(int)

# Crear llave surrogate incremental
orders["order_key"] = range(1, len(orders) + 1)

# Seleccionar únicamente las columnas finales que existirán en SQL
orders = orders[[
    "order_key",
    "order_id",
    "order_date_key",
    "ship_date_key"
]]

# Guardar CSV
orders.to_csv("data_clean/dim_order.csv", index=False)








df.to_csv("data_clean/clean_superstore.csv", index=False)
