from student_reg_inbuilt.write_file import write_json
def delete_student_data(student_list,json_file):
    contact_number_search=input("Please enter the contact of the student: ")
    if contact_number_search.isdigit():
        contact_number_search=int(contact_number_search)
        for item in student_list:
            if item["contact"]==contact_number_search:
                print(item)
                student_list.remove(item)
                write_json(json_file,student_list)
                print("Data Deleted Successfully")

