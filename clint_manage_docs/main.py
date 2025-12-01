import time
import uuid
import json
import clint_menu
import clint_registration
clint_list=[]






while 1:
    clint_menu_choise=clint_menu.clint_menu()
    if clint_menu_choise==1:
        clint_registration.clint_registration(clint_list)
    elif clint_menu_choise==2:
        print("Exiting.......")
        time.sleep(3)
        print("Exited Successfully")
        break
    else:
        print(" Wrong Input , Please Enter 1 or 2 ")


