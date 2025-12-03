import json
def email_searching(clint_details):
    email_search_entry=input("please enter the email : ")
    for item in clint_details:
        if item["email"].lower()==email_search_entry.lower():
            print(json.dumps(item,indent=4))
            break

    else:
        print(" NOT FOUND ")        