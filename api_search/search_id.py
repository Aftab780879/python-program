def user_searching(coffee):
    
    if len(coffee)>0:
        id_entry=input("Please enter the Id: ")
        if id_entry.isdigit():
            id_entry=int(id_entry)
            for item in coffee:
                if id_entry == item["id"]:
                    print(item)
                    break
                    
            else:
                    print("not found")