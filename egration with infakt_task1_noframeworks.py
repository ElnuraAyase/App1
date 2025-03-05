import request # for hhttp request

API_KEY = 'any-api_key'        # any secure api key
BASE_URL = 'http//_ invoices'   # creating inv

headers = { "Content-Type":"application/json",  # jsn data sending
           "X-inFakt-ApiKey":API_KEY }

'''
if many  API requests  to use dfferent headers and different requests 
 beg_headers = { "Content-Type": "application/json"}
 autho_headers = { "X-inFakt-ApiKey": API_KEY
 }
 and merging them 
 headers = {**beg_headers, **autho_headers}

 '''
