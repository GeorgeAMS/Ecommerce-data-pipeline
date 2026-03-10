import requests
import pandas as pd

# URL de la API
url = "https://fakestoreapi.com/products"

# Hacer request a la API
response = requests.get(url)

# Convertir a JSON
data = response.json()

# Convertir a DataFrame
df = pd.DataFrame(data)

# Mostrar primeras filas
print(df)

print("\nColumnas del dataset:")
print(df.columns)
print(df.describe())

print(df.columns)
print(df.dtypes)
print(df.isnull().sum())
print(df.describe())

#id - title - price - description - category - image - rating 
#Se observa que el campo rating es un json, se debe de normalizar si queremos utilizar

df["rating_rate"] = df['rating'].apply(lambda x: x['rate']) 
df["rating_count"] = df['rating'].apply(lambda x: x['count']) 


df = df[["id", "title", "price", "category", "rating_rate", "rating_count"]] #Seleccionar columnas 

# Renombrar columnas
df.columns = [
    "product_id",
    "product_name",
    "price",
    "category",
    "rating_rate",
    "rating_count"
]
print(df.shape)