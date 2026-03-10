from api.extract_products import extract_products
from etl.transform_products import transform_products
from etl.load_products import load_products
from etl.generate_customers import generate_customers
from etl.generate_sales import generate_sales
# 1 extraer
df = extract_products()

# 2 transformar
df = transform_products(df)

# 3 cargar
load_products(df)
generate_sales()