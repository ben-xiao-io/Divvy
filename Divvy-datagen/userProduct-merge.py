import json
import pandas as pd
import random
import numpy as np

loproducers = None
with open('producerids.json') as f:
    loproducers = json.load(f)

print(loproducers)

def gen_purchase_hist(max_hist):
    product_df = pd.read_csv('product-cleaned.csv')

    # we want to generate non repeating indexes and have enough
    # for zero value argumnets. We generate a list of random
    # non repeating numbers with a length of max_hist
    rand_list = random.sample(range(product_df.shape[0]), max_hist) 

    # we randomly pick an valid amount of indexes to create a subset
    # for the zero arguments.
    sub_rand_list = random.sample(rand_list, max(int(len(rand_list)/2), 5))
    zero_args_list = np.array(sub_rand_list)

    # The non zero list is essential the set difference between the 
    # rand_list and zero_arg_list which is a subset of rand_list
    non_zero_args_list = np.setdiff1d(np.array(rand_list).tolist(), zero_args_list)

    # We then convert both back into numpy arrays
    non_zero_args_list = np.array(non_zero_args_list).tolist()
    zero_args_list = np.array(zero_args_list).tolist()
    
    purchase_history = []
    for row in non_zero_args_list:

        # select row by int
        product = product_df.iloc[[row]]
        single_purchase = {
            'listPrice' : product.iloc[0]['list_price'],
            'salePrice' : product.iloc[0]['sale_price'],
            'producer' : product.iloc[0]['brand'],
            'producerNum' : loproducers.index(product.iloc[0]['brand']),
            'productid' : product.iloc[0]['uniq_id'], 
            'productUrl' : product.iloc[0]['product_url'],
            'productImageUrl' : product.iloc[0]['product_image_urls'],
            'amountPaid' : round((product.iloc[0]['sale_price'] * random.randint(10, 100)), 2),
            'bought' : 1
            }
            
        purchase_history.append(single_purchase)
    
    for row in zero_args_list:

        # select row by int
        product = product_df.iloc[[row]]
        single_zero_purchase = {
            'listPrice' : product.iloc[0]['list_price'],
            'salePrice' : product.iloc[0]['sale_price'],
            'producer' : product.iloc[0]['brand'],
            'producerNum' : loproducers.index(product.iloc[0]['brand']),
            'productid' : product.iloc[0]['uniq_id'], 
            'productUrl' : product.iloc[0]['product_url'],
            'productImageUrl' : product.iloc[0]['product_image_urls'],
            'amountPaid' : 0,
            'bought' : 0
            }
            
        purchase_history.append(single_zero_purchase)
    return purchase_history


data = json.load(open('user-data.json'))
temp = []
for user in data:
    if user['purchase_history'] != None:
        continue
    temp += gen_purchase_hist(random.randint(8, 25))



with open('user-product-data.json', 'w') as outfile:
    json.dump(temp, outfile)