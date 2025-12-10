from student_reg_inbuilt.write_file import write_json
from student_reg_inbuilt.update_menu import update_menu_view
import json

def update_file(student_list,json_file):
    if len(student_list)>0:
        contact_number_search=input("Please enter the contact of the student: ")
        if contact_number_search.isdigit():
            contact_number_search=int(contact_number_search)
            for item in student_list:
                if item["contact"]==contact_number_search:
                    print(json.dumps(item))
                    while 1:
                        update_menu_choice=update_menu_view()
                        if update_menu_choice==1:
                            new_first_name=input("Please enter The correct First Nmae: ").lower()
                            if new_first_name.isalpha():
                                item["first_name"]=new_first_name
                                print(json.dumps(item))
                                write_json(json_file,student_list)
                                print("\nFirst name Updated SuccessFully\n")
                        elif update_menu_choice==2:
                            new_last_name=input("Please enter The correct Last Nmae: ").lower()
                            if new_last_name.isalpha():
                                item["last_name"]=new_last_name
                                print(json.dumps(item))
                                write_json(json_file,student_list)
                                print("\nLast name Updated SuccessFully\n")
                        elif update_menu_choice==3:
                            new_address=input("Please enter Your new address: ").lower()
                            item["address"]=new_address
                            print(item)
                            write_json(json_file,student_list)
                            print("\nAddress updated Successfully\n")
                        elif update_menu_choice==4:
                            new_contact_number=input("Please enter the new contact number: ")
                            if new_contact_number.isdigit():
                                new_contact_number=int(new_contact_number)
                                item["contact"]=new_contact_number
                                print(item)
                                write_json(json_file,student_list)
                                print("\nContact Updated Successfully\n")
                        elif update_menu_choice==5:
                            break
                        else:
                            ("\nWrong Input, Please try numbers 1 to 5")        
    else:
        print("\nThere Is no data For Update")

