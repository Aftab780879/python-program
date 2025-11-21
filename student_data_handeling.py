student_list=[]

def user_menu():
    print("\n********** USER MENU **********")
    print("1. Student Registration")
    print("2. Search")
    print("3. Delete")
    print("4. Exit")
    print("5. View Records\n")
    user_menu_choise=input("Please Enter Your Choise: ")

    if user_menu_choise.isdigit():
        user_menu_choise=int(user_menu_choise)
        


    return user_menu_choise

def student_registration():
    student_disc={}
    print(f"********* Student Data *********")
    student_disc["id"]= input("please enter the ID: ")
    student_disc["name"]=input("please enter the students NAME: ")
    student_disc["address"]=input("please enter the students ADDRESS: ")
    student_disc["contact"]=input("Please enter your contact number: ")
    student_disc["qualification"]=[]
    qualification_disc={}
    qualification_disc["Qualification"]=input("please enter your QUALIFICATION(only use small letters): ")
    qualification_disc["Year"]=input("please enter the year:  ")
    student_disc["qualification"].append(qualification_disc)
    extra_qualification()
    student_list.append(student_disc)


def extra_qualification():
    while 1:
        print("\ndo you want to enter more qualification")
        print("Press 1. To Add More Qualification")
        print("press 2. To Continue\n")
        qualification_entry=input("Please enter your choise: ")
        if qualification_entry.isdigit():
            qualification_entry=int(qualification_entry)
        if qualification_entry==1:
            qualification_disc={}
            qualification_disc["Qualification"]=input("please enter your QUALIFICATION(only use small letters): ")
            qualification_disc["Year"]=input("please enter the year:  ")
            student_disc["qualification"].append(qualification_disc)
        elif qualification_entry==2:
            break   
        else:
            print("invalid choise")    

def user_searching():
    search_found=0
    while 1:

        print("********* REPORT *********")
        print("Press 1. To Find details with Contact")
        print("Press 2. To Find details with Qualification")
        print("press 3. To Exit")
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

def user_deleting():
    user_delete_choise=input("Please Enter the contact number of the user you want to delete: ")
    for item in student_list:   
        if item["contact"]==user_delete_choise:
                print("ITEM DELETED SUCCESSFULLY")
                student_list.remove(item)
        else:
                print("not found")

def user_records():
    if len(student_list)>0:
        print(student_list)
    else:
        print("\nThe Records are Empty\n")    



def all_operation():

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
            user_records()
        else:
            print(" WRONG INPUT ! , please try again")


all_operation()