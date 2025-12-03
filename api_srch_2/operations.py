import requests
from api_srch_2.id_search import user_searching
from api_srch_2.email_search import email_searching
from api_srch_2.address_srch import address_searching
import json

response=requests.get("https://jsonplaceholder.typicode.com/users")
clint_details=response.json()
def operations():

    while 1:
        print("\n********* SEARCH MENU *********")
        print("Press 1. To Find details with Id")
        print("Press 2. To Find details with email")
        print("Press 3. To Find details with address")
        print("Press 4. To Exit")

        search_choice=input("please enter your choice: ")
        if search_choice.isdigit():
            search_choice=int(search_choice)
            if search_choice==1:
                user_searching(clint_details)
            elif search_choice==2:
                email_searching(clint_details) 
            elif search_choice==3:
                address_searching(clint_details)
            elif search_choice==4:
                break
            else:
                print("wrong input")
        else:
            print("Please Enter A number not letter")