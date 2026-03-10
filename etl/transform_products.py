import pandas as pd

def transform_products(df):

    # extraer datos del rating
    df["rating_rate"] = df["rating"].apply(lambda x: x["rate"])
    df["rating_count"] = df["rating"].apply(lambda x: x["count"])

    # seleccionar columnas
    df = df[["id", "title", "price", "category", "rating_rate", "rating_count"]]

    # renombrar columnas
    df.columns = [
        "product_id",
        "product_name",
        "price",
        "category",
        "rating_rate",
        "rating_count"
    ]

    return df