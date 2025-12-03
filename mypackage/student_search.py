def user_searching(student_list):
    if len(student_list)>0:

        search_found=0
        while 1:

            print("********* REPORT *********")
            print("Press 1. To Find details with Contact")
            print("Press 2. To Find details with Qualification")
            print("press 3. To Go Back To MAIN MENU")
            search_entry=input("Please enter Your choise: ")
            if search_entry.isdigit():
                search_entry=int(search_entry)
                if search_entry==1:
                    contact_entry=input("Please enter the Contact: ")
                    for item in student_list:
                        if item["contact"]==contact_entry:
                            print(item)
                        else:
                            print("not found")    
                elif search_entry==2:
                    qualification_search=input("please enter the qualification from which you want to search(use alphabets only): ")     
                    for item in student_list:
                        for value in item["qualification"]:
                            if value["Qualification"].lower() == qualification_search.lower():
                                print(item)
                                search_found+=1
                                if search_found==0:
                                    print("NO DATA FOUND")
                       

                elif search_entry==3:
                    break               
                else:
                    print("INVALID INPUT") 
            else:
                print("INVALID INPUT")        
    else:
        print("No Records to Show")