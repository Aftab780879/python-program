def clint_menu():
    
    print("\n********CLINT MENU********")
    print("1. CLINT REGISTRATION")
    print("2. EXIT \n")
    clint_menu_choice=input("Please enter your choice: ")
    if clint_menu_choice.isdigit():
        clint_menu_choice=int(clint_menu_choice)

    return clint_menu_choice  