import psycopg2

def load_products(df):

    conn = psycopg2.connect(
        host="localhost",
        database="ecommerce_pipeline",
        user="postgres",
        password="123456789"
    )

    cur = conn.cursor()

    for _, row in df.iterrows():

        cur.execute(
            """
            INSERT INTO products
            (product_id, product_name, price, category, rating_rate, rating_count)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (product_id) DO NOTHING
            """,
            (
                row.product_id,
                row.product_name,
                row.price,
                row.category,
                row.rating_rate,
                row.rating_count
            )
        )

    conn.commit()

    cur.close()
    conn.close()

    print("Datos cargados correctamente")