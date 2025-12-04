import json
def address_searching(clint_details):
    try:
        while 1:
            print("\n1. To Find details with street")
            print("2. To Find details with suite")
            print("3. To Find details with city")
            print("4. To Find details with zip-code")
            print("5. To Find details with Latitude")
            print("6. To Find details with Longitude")
            print("7. To go Back")

            address_searching_choice=input("Please enter your Choice: ")
            if address_searching_choice.isdigit():
                address_searching_choice=int(address_searching_choice)
                if address_searching_choice==1:
                    street_search_entry=input("please enter the street: ")
                    for item in clint_details:
                        
                        if item["address"]["street"].lower()==street_search_entry.lower():
                            print(json.dumps(item,indent=4))
                            break
                    else:
                        print("Not Found")   

                elif address_searching_choice==2:
                    suite_search_entry=input("please enter the suite: ") 
                    for item in clint_details:
                        if item["address"]["suite"].lower()==suite_search_entry.lower():
                            print(json.dumps(item,indent=4))
                            break
                    else:
                        print("Not Found")     

                elif address_searching_choice==3:
                    city_search_entry=input("Please enter the city: ")
                    for item in clint_details:
                        if item["address"]["city"].lower()==city_search_entry.lower():
                            print(json.dumps(item,indent=4)) 
                            break
                    else:
                        print("NOT FOUND")

                elif address_searching_choice==4:
                    zipcode_search_entry=input("please enter the Zip-Code: ")
                    for item in clint_details:
                        if item["address"]["zipcode"]==zipcode_search_entry:  
                            print(json.dumps(item,indent=4))   
                            break
                    else:
                        print("NOT FOUND") 
                elif address_searching_choice==5:
                    latitude_search_entry=input("please enter the Latitude: ")
                    for item in clint_details:
                        if item["address"]["geo"]["lat"]==latitude_search_entry:
                            print(json.dumps(item,indent=4))
                            break
                    else:
                        print("NOT FOUND")  

                elif address_searching_choice==6:
                    longitude_search_entry=input("please enter the Longitude: ")
                    for item in clint_details:
                        if item["address"]["geo"]["lng"]==longitude_search_entry:
                            print(json.dumps(item,indent=4))
                            break
                    else:
                        print("NOT FOUND")           


                elif address_searching_choice==7:
                    break
                else:
                    print("WRONG INPUT , PLEASE TRY AGAIN")                              
            else:
                print("Please enter a digit not alphabet")  
    except Exception:
        print("Service not Available, Try After Some Time")