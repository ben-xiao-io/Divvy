import pandas as pd
import json

loproducers = None
with open('producerids.json') as f:
    loproducers = json.load(f)


def clean_csv():
    file = open('product-cleaned.csv', encoding="utf-8", errors='ignore')
    product_df = pd.read_csv(file).replace(['\䋢'], [''], regex=True)

    product_list = []
    for index, row in product_df.iterrows():
        temp = {
            'uniq_id' : row['uniq_id'],
            'name_title' : row['name_title'],
            'description' : row['description'],
            'list_price' : row['list_price'],
            'sale_price' : row['sale_price'],
            'product_url' : row['product_url'],
            'product_image_urls' : row['product_image_urls'],
            'producer' : row['brand'],
            'producerNum' : loproducers.index(row['brand'])
        }
        product_list.append(temp)

    with open('producerids.json', 'w') as outfile:
        json.dump(product_list, outfile)


def attachIncId():
    file = open('product-cleaned.csv')
    product_df = pd.read_csv(file)

    print(product_df.shape[0])

    existing = []
    loproducers = []
    for row_count in range(product_df.shape[0]):
        if product_df.iloc[row_count]['brand'] in existing:
            continue
        
        #loproducers.append({'producer_num' : row_count, 'producer' : product_df.iloc[row_count]['brand']})
        existing.append(product_df.iloc[row_count]['brand'])
    
    with open('producerids.json', 'w') as outfile:
        json.dump(existing, outfile)


clean_csv()