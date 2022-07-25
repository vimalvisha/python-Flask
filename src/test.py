
import json
import requests

# app=Flask(_name_)
base_url='http://127.0.0.1:5000/students'

input = {
    "Full_Name":"Abc", 
    "Mobile_No": 756478382722, 
    "Reg_No" : 10304015793, 
    "Branch": "EC"}
# resp=json.dumps(input)
response = requests.post(base_url, data=json.dumps(input)).json()
print(response)
