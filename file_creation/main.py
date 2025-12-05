import os
import time

folder_path=r"C:\File Folder"


file_number=input("Please enter the number of files you want to create: ")
if file_number.isdigit():
    file_number=int(file_number)

    for number in range(file_number):
        file_name=input(f"\nPlease enter the file {number+1} name: ").lower()+(".txt")
        
        file_path=os.path.join(folder_path,file_name)
        with open(file_path,'w') as file:
            file.write("My name is aftab")
        print("\nCreating.............")
        time.sleep(2)
        print(f"\nYour file name {file_name} created Successfully")

    print("\nAll Files Created Successfully")        
else:
    print("Invalid Input , PLease use Numbers")            

