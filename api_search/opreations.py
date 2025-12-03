import requests
from api_search.search_id import user_searching
from api_search.search_ingredient import search_ingredients
import json

response=requests.get("https://api.sampleapis.com/coffee/hot")
coffee=response.json()
def operations():

    while 1:
        print("\n********* REPORT *********")
        print("Press 1. To Find details with Id")
        print("Press 2. To Find details with ingredients")
        print("Press 3. To Exit")

        search_choice=input("please enter your choice: ")
        if search_choice.isdigit():
            search_choice=int(search_choice)
            if search_choice==1:
                user_searching(coffee)
            elif search_choice==2:
                search_ingredients(coffee)  
            elif search_choice==3:
                break
            else:
                print("wrong input")
