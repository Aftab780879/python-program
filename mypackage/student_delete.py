def user_deleting(student_list):
    if len(student_list)>0:

        user_delete_choise=input("Please Enter the contact number of the user you want to delete: ")
        for item in student_list:   
            if item["contact"]==user_delete_choise:
                    print("ITEM DELETED SUCCESSFULLY")
                    student_list.remove(item)
            else:
                    print("not found")
    else:
        print("No Records to Show") 