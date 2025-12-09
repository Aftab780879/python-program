from student_reg_inbuilt.read_file import read_json
import uuid
import json
def registration(student_list):
    json_file=r"C:\indixpert\python\python-practice\student_reg_inbuilt\student.json"
    data=read_json()
    student_list=json.loads(data)

    student_dict={}
    
    student_dict["id"]=uuid.uuid4().hex[:8]
    student_dict["name"]=input("please enter student name: ")
    student_dict["address"]=input("please enter student address: ")
    while 1:
         
        student_dict["contact"]=input("please enter contact number: ")
        if student_dict["contact"].isdigit and len(student_dict["contact"])==10:
            student_dict["contact"]=int(student_dict["contact"])
            student_list.append(student_dict)
            with open(json_file,'w') as file:
                file.write(json.dumps(student_list,indent=4))
            print("Successfully added student")
            break

        else:
                print("Invalid Contact Number") 
          
