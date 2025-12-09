import os

def read_json():
    json_file=r"C:\indixpert\python\python-practice\student_reg_inbuilt\student.json"

    if os.path.exists(json_file):
        with open(json_file,'r') as file:
           data= file.read().strip()
           if data=="":
               return "[]"
           return data
    else:
        with open(json_file,'w') as file:
            file.write("[]")
            return "[]"
       
