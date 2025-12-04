import json


def email_searching(clint_details):
    try:

        email_search_entry=input("please enter the email : ")
        for item in clint_details:
            if item["email"].lower()==email_search_entry.lower():
                print(json.dumps(item,indent=4))
                break

        else:
            print(" NOT FOUND ")  
    except Exception:
        print("Service not Available, Try After Some Time")              