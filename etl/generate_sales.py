import psycopg2
import random
from datetime import datetime

def generate_sales():

    conn = psycopg2.connect(
        host="localhost",
        database="ecommerce_pipeline",
        user="postgres",
        password="123456789"
    )

    cur = conn.cursor()

    # obtener ids reales de productos
    cur.execute("SELECT product_id FROM products")
    product_ids = [row[0] for row in cur.fetchall()]

    # obtener ids reales de clientes
    cur.execute("SELECT customer_id FROM customers")
    customer_ids = [row[0] for row in cur.fetchall()]

    for i in range(30):

        product_id = random.choice(product_ids)
        customer_id = random.choice(customer_ids)

        quantity = random.randint(1,3)
        sale_date = datetime.today()

        cur.execute(
            """
            INSERT INTO sales
            (product_id, customer_id, quantity, sale_date)
            VALUES (%s,%s,%s,%s)
            """,
            (product_id, customer_id, quantity, sale_date)
        )

    conn.commit()

    cur.close()
    conn.close()

    print("Ventas generadas")