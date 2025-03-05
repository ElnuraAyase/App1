import request # for hhttp request

API_KEY = 'any-api_key'        # any secure api key
BASE_URL = 'http//_ invoices'   # creating inv , API endpoint

headers = { "Content-Type": "application/json",  # jsn data sending
           "X-inFakt-ApiKey":API_KEY }


'''
if many  API requests - to use dfferent headers and different requests 
 beg_headers = { "Content-Type": "application/json"}
 autho_headers = { "X-inFakt-ApiKey": API_KEY
 }
 and merging them 
 headers = {**beg_headers, **autho_headers}

 '''
# info from invoice
invoice_info = {
           "cl_name": "Maria ",
           'cl_tax': "33443545",
           "cl_adress" : "Sl. Polsce 12",
           'cl_city": "Warsaw",
           "positions": [ {
                      "name": "Mleko",
                      "tax": "2",
                      "price": "3.36",
                      "quantity": "1"}
                        ],
           "data": "2025-03-05"
           "payment_type": "cash"
}

# sending  invoice reqest
response = requests.post(BASE_URL, json=invoice_data, headers=headers)

# checking 

if response.status_code == 201
print("Invoice created successfully:", response.json())
else: 
print("Error:", response.status_code, response.text)

                      
           

