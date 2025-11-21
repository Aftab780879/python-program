def user_menu():
    print("1. Student Registration")
    print("2. Search")
    print("3. Delete")
    print("4. Exit")
    print("5. View Records")

    user_menu_choise=int(input("Please Enter Your Choise: "))
    return user_menu_choise

def student_registration():
    student_disc={}
    print(f"********* Student Data *********")
    student_disc["id"]= int(input("please enter the ID: "))
    student_disc["name"]=input("please enter the students NAME: ")
    student_disc["address"]=input("please enter the students ADDRESS: ")
    student_disc["contact"]=input("Please enter your contact number: ")
    student_disc["qualification"]=[]
    qualification_disc={}
    qualification_disc["Qualification"]=input("please enter your QUALIFICATION: ")
    qualification_disc["Year"]=input("please enter the year:  ")
    student_disc["qualification"].append(qualification_disc)
    while 1:
        print("do you want to enter more qualification")
        print("Press 1. To Add More Qualification")
        print("press 2. To Continue")
        qualification_entry=int(input("Please enter your choise: "))
        if qualification_entry==1:
            qualification_disc={}
            qualification_disc["Qualification"]=input("please enter your QUALIFICATION: ")
            qualification_disc["Year"]=input("please enter the year:  ")
            student_disc["qualification"].append(qualification_disc)
        elif qualification_entry==2:
            break   
        else:
            print("invalid choise")
    student_list.append(student_disc)

def user_searching():
    while 1:

        print("********* REPORT *********")
        print("Press 1. To Find details with Contact")
        print("Press 2. To Find details with Qualification")
        print("press 3. To Exit")
        search_entry=int(input("Please enter Your choise: "))
        if search_entry==1:
            contact_entry=input("Please enter the Contact: ")
            for item in student_list:
                if item["contact"]==contact_entry:
                    print(item)
                else:
                    print("not found")    
        elif search_entry==2:
            qualification_search=input("please enter the qualification from which you want to search: ")     
            for item in student_list:
                for value in item["qualification"]:
                    if value["Qualification"].lower() == qualification_search.lower():
                        print(item) 
        elif search_entry==3:
            break               
        else:
            print("INVALID INPUT")  

def user_deleting():
    user_delete_choise=int(input("Please Enter the user index number you want to delete: "))
    student_list.pop[user_delete_choise]



student_list=[]
while 1:
    user_menu_choise=user_menu()
    if user_menu_choise==4:
        break
    elif user_menu_choise==1:
        student_registration()
    elif user_menu_choise==2:
        user_searching()
    elif user_menu_choise==3:
        user_deleting()
    elif user_menu_choise==5:
        print(student_list)
    else:
        print(" WRONG INPUT ! , please try again")


