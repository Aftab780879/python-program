import requests
import json


response=requests.get("https://jsonplaceholder.typicode.com/users")
client_details=response.json()

client_dict={
    "clint_details":client_details
}
print(json.dumps(client_dict,indent=4))