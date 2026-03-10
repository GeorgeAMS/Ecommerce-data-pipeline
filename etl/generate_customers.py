import psycopg2
import random
from datetime import datetime, timedelta

names = [
    "Sara Monsalve", "Sara Jimenez", "Sara Echeverry", "Sebastian Tunjuelo", "Sebastian Montoya",
    "Jorge Martinez", "Michael Colmenares", " Juan Pablo Jimenez", "Juanita Galindo", "Jeronimo Ochoa",
    "Diego Martinez", "Jose Arrieta", "Laura Jimenez", "Nataly Alvarez", "Yuliza Meza", "Juan Alvarez",
    "Steven Pico", "El viejo Fabi"
]
cities = [
    "Bogota", "Medellin","Montelibano","Monteria","Barranquilla","Cartagena","Caucasia","Don Matias",
    "Bello", "San Andres Islas", "Ure"
]

def generate_customers():
    conn = psycopg2.connect(
        host="localhost",
        database="ecommerce_pipeline",
        user="postgres",
        password="123456789"
    )

    cur = conn.cursor()

    for i in range(30):
        name = random.choice(names)
        city = random.choice(cities)
        country = "Colombia"

        days_ago = random.randint(1,365)
        reg_date = datetime.today() - timedelta(days=days_ago)

        cur.execute(
            """
            INSERT INTO customers
            (customer_name, city, country, registration_date)
            VALUES (%s,%s,%s,%s)
            """,
            (name, city, country, reg_date)
        )
    conn.commit()

    cur.close()
    conn.close()

    print("Clientes Generados")