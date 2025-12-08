import os
import json

json_file=r"C:\indixpert\python\python-practice\file_creation\file_no.json"
folder_path=r"C:\File Folder"

if os.path.exists(json_file):
    with open(json_file,"r") as file:
        data=json.load(open(json_file))
        last_count=data["file_count"]

else:
    last_count=0        


file_number=input("Please enter the number of files you want to create: ")
file_name="alpha"
if file_number.isdigit():
    file_number=int(file_number)
    

    for number in range(file_number):
        last_count+=1
        
        file_path=os.path.join(folder_path,file_name+(f"{last_count}.txt"))
        with open(file_path,'w') as file:
            file.write("My name is aftab")
            

    print("\nAll Files Created Successfully") 
    json.dump({"file_count":last_count},open(json_file,"w"))      
else:
    print("Invalid Input , PLease use Numbers")            

