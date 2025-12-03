def user_menu():
    print("\n********** USER MENU **********")
    print("1. Student Registration")
    print("2. Search")
    print("3. Delete")
    print("4. Exit")
    print("5. View Records\n")
    user_menu_choise=input("Please Enter Your Choise: ")

    if user_menu_choise.isdigit():
        user_menu_choise=int(user_menu_choise)
        
    return user_menu_choise