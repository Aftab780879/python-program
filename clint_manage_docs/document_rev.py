def docs_review(clint_dict,clint_list):
    while 1:

            print("\n1. Review Documents")
            print("2. BACK")
            review_choice=input("Please enter Your Choice: ")
            if review_choice.isdigit():
                review_choice=int(review_choice)
                if review_choice==1:
                    print("------------------------------------------")
                    print("|               USER DETAILS             |")
                    print("------------------------------------------")
                    print(f"ID               =  {clint_dict["id"]}")
                    print(f"NAME             =  {clint_dict["first_name"]} {clint_dict["last_name"]}")
                    print(f"ADDRESS          =  {clint_dict["address"]}")
                    print("\n*************   DOCUMENTS   *************")
                    aadhar=clint_dict["documents"][0]
                    print("\n   ********** AADHAR DETAILS **********")
                    print(f"AADHAR NUMBER    =  {aadhar["aadhar_number"]}")
                    print(f"AADHAR IMAGE     =  {aadhar["aadhar_image"]}")
                    pan=clint_dict["documents"][1]
                    print("\n ************* PAN DETAILS *************")
                    print(f"PAN NUMBER       =  {pan["pan_number"]}")
                    print(f"PAN IMAGE        =  {pan["pan_image"]}")
                    voter_id=clint_dict["documents"][2]
                    print("\n************* VOTER ID DETAILS *************")
                    print(f"VOTER ID NUMBER  =  {voter_id["voter_id_number"]}")
                    print(f"VOTER ID IMAGE   =  {voter_id["voter_id_image"]}")

                    while 1:
                        print("\n\n1. Save The Details")
                        print("2. Delete ")
                        save_details_choice=input("Please Enter Your Choice: ")
                        if save_details_choice.isdigit():
                            save_details_choice=int(save_details_choice)
                            if save_details_choice==1:
                                clint_list.append(clint_dict)
                                print("Details Saved Successfully!")
                                return
                            elif save_details_choice==2:
                                print(" Your Details Were not Saved")
                                return
                            else:
                                print(" Wrong Input , Please Try Again")



                elif review_choice==2:
                    break
                else:
                    print("Wrong Input , Please Try Again")
