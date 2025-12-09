
def search_file(student_list):
    contact_number_search=input("Please enter the contact of the student: ")
    if contact_number_search.isdigit():
        contact_number_search=int(contact_number_search)
        for item in student_list:
            if item["contact"]==contact_number_search:
                print(item)
