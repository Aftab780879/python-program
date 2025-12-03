from .user_menu import user_menu
from .student_reg import student_registration
from .student_search import user_searching
from .student_delete import user_deleting
from .records import user_records


student_list=[]
def all_operation():

    while 1:
        user_menu_choise=user_menu()
        if user_menu_choise==4:
            break
        elif user_menu_choise==1:
            student_registration(student_list)
        elif user_menu_choise==2:
            user_searching(student_list)
        elif user_menu_choise==3:
            user_deleting(student_list)
        elif user_menu_choise==5:
            user_records(student_list)
        else:
            print("WRONG INPUT ! , please try again")
