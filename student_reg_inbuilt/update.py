from student_reg_inbuilt.write_file import write_json

def update_file(student_list,json_file):
    contact_number_search=input("Please enter the contact of the student: ")
    if contact_number_search.isdigit():
        contact_number_search=int(contact_number_search)
        for item in student_list:
            if item["contact"]==contact_number_search:
                print(item)
                new_contact_number=input("Please enter the new contact number: ")
                if new_contact_number.isdigit():
                    new_contact_number=int(new_contact_number)
                    item["contact"]=new_contact_number
                    print(item)
                    write_json(json_file,student_list)
                    print("Data Updated Successfully")


