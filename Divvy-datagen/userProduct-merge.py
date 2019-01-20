import json
import pandas as pd
import random

def gen_purchase_hist(max_hist):
    product_df = pd.read_csv('product-cleaned.csv')
    
    purchase_history = []
    for hist_count in range(max_hist):
        product = product_df.iloc[[random.randint(0, product_df.shape[0] - 1)]]
        single_purchase = {
            'productid' : product.iloc[0]['uniq_id'], 
            'amountPaid' : round((product.iloc[0]['sale_price'] * random.randint(10, 100)), 2)
            }
            
        purchase_history.append(single_purchase)
    return purchase_history


data = json.load(open('user-data.json'))
for user in data:
    if user['purchase_history'] != None:
        continue

    user['purchase_history'] = gen_purchase_hist(random.randint(5, 25))

with open('user-product-data.json', 'w') as outfile:
    json.dump(data, outfile)