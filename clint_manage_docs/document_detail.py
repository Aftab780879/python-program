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
                        voter_dict["voter_id_number"]=input("\nPlease Enter Your VOTER ID: ")
                        if voter_dict["voter_id_number"].isalnum and len(voter_dict["voter_id_number"])==10:
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
               
    return docs_list
