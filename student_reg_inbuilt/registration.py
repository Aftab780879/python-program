from student_reg_inbuilt.write_file import write_json
import uuid
import json
def registration(student_list):
    json_file=r"C:\indixpert\python\python-practice\student_reg_inbuilt\student.json"
    

    student_dict={}
    
    student_dict["id"]=uuid.uuid4().hex[:8]
    student_dict["name"]=input("please enter student name: ")
    student_dict["address"]=input("please enter student address: ")
    while 1:
         
        student_dict["contact"]=input("please enter contact number: ")
        if student_dict["contact"].isdigit and len(student_dict["contact"])==10:
            student_dict["contact"]=int(student_dict["contact"])
            student_list.append(student_dict)
            write_json(json_file,student_list)
            print("Successfully added student")
            break

        else:
                print("Invalid Contact Number") 
          
