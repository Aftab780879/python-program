def student_registration(student_list):
    student_disc={}
    student_disc["qualification"]=[]
    qualification_disc={}
    print(f"********* Student Data *********")
    student_disc["id"]= input("please enter the ID: ")
    student_disc["name"]=input("please enter the students NAME: ")
    student_disc["address"]=input("please enter the students ADDRESS: ")
    student_disc["contact"]=input("Please enter your contact number: ")
    
    qualification_disc["Qualification"]=input("please enter your QUALIFICATION(only use small letters): ")
    qualification_disc["Year"]=input("please enter the year:  ")
    student_disc["qualification"].append(qualification_disc)

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
    student_list.append(student_disc)
