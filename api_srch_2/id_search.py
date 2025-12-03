import json
def user_searching(clint_details):
    
    if len(clint_details)>0:
        id_entry=input("Please enter the Id: ")
        if id_entry.isdigit():
            id_entry=int(id_entry)
            for item in clint_details:
                if id_entry == item["id"]:
                    print(json.dumps(item,indent=4))
                    break
                    
            else:
                    print("not found")
        else:
            print("Please enter a digit not alphabet")            