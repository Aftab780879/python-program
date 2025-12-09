from student_reg_inbuilt.menu import reg_menu
from student_reg_inbuilt.registration import registration
student_list=[]
def operations():
    while 1:
        reg_menu_choice=reg_menu()
        if reg_menu_choice==1:
            registration(student_list)
        elif reg_menu_choice==2:
            break
        else:
            print("Wrong Input , Please enter 1 or 2")