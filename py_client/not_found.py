import requests
import json

endpoint = 'http://localhost:8000/api/products/132321323312312312/'

get_response = requests.get(endpoint)
print(get_response.json())
