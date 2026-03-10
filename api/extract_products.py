import requests
import pandas as pd

def extract_products():

    url = "https://fakestoreapi.com/products"

    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame(data)

    return df