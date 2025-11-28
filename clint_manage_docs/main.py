import time
import uuid
import json
clint_list=[]


def clint_menu():
    
    print("\n********CLINT MENU********")
    print("1. CLINT REGISTRATION")
    print("2. EXIT \n")
    clint_menu_choice=input("Please enter your choice: ")
    if clint_menu_choice.isdigit():
        clint_menu_choice=int(clint_menu_choice)

    return clint_menu_choice            

def clint_registration():
    clint_dict={}
    clint_dict["id"]=uuid.uuid4().hex[:10]
    clint_dict["name"]=input("Please Enter Your Name: ")
    if clint_dict["name"].isalpha():
        clint_dict["address"]=input("Please Enter Your Address: ")
        docs_list=document_details()
        clint_dict["documents"]=docs_list
        clint_list.append(clint_dict)


    else:
        print("Please Register Again")    

def document_details():
    while 1:
        print("\n1. Next") 
        print("2. Back\n")
        document_details_choice=input("Please enter Your Choice: ")
        if document_details_choice.isdigit():
            document_details_choice=int(document_details_choice)
            if document_details_choice==1:
                docs_list=[]
                aadhar_dict={}
                pan_dict={}
                voter_dict={}
                aadhar_dict["aadhar_number"]=input("\nPlease Enter Your AADHAR NUMBER: ")
                if aadhar_dict["aadhar_number"].isdigit() and len(aadhar_dict["aadhar_number"])==12:
                    aadhar_dict["aadhar_image"]=input("Please enter Your Aadhar image LINK: ")
                    docs_list.append(aadhar_dict)
                    pan_dict["pan_number"]=input("\nPlease Enter Your PAN NUMBER: ")
                    if pan_dict["pan_number"].isalnum and len(pan_dict["pan_number"])==10:
                        pan_dict["pan_image"]=input("Please enter Your PAN image LINK: ")
                        docs_list.append(pan_dict)
                        voter_dict["voter_id"]=input("\nPlease Enter Your VOTER ID: ")
                        if voter_dict["voter_id"].isalnum and len(voter_dict["voter_id"])==10:
                            voter_dict["voter_id_image"]=input("Please enter Your VOTER ID image LINK: ")
                            docs_list.append(voter_dict)
                            break
                    
                        else:
                            print("Please enter the correct VOTER ID")    
                    else:
                        print("Please Enter The correct pan number using Alphabet and Numbers")    
                else:
                    print("WRONG INPUT , Please Enter a 12 digit Aadhar number")

            elif document_details_choice==2:
                break
            else:
                print("Wrong Input, Please try Again")
               
    return document_details_choice,docs_list


while 1:
    clint_menu_choise=clint_menu()
    if clint_menu_choise==1:
        clint_registration()
    elif clint_menu_choise==2:
        print("Exiting.......")
        time.sleep(3)
        print("Exited Successfully")
        print(json.dumps(clint_list,indent=4))
        break
    else:
        print(" Wrong Input , Please Enter 1 or 2 ")


