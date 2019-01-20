import pandas as pd

clean_csv('product-datagen.csv')

def clean_csv(filename):
    file = open(filename, encoding="utf-8", errors='ignore')
    product_df = pd.read_csv(file).replace(['\䋢'], [''], regex=True)
    product_df.to_csv(filename + '-cleaned.csv')