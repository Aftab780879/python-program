def reg_menu():
    print("\n1. Registration")
    print("2. Exit")

    reg_menu_choice=input("please enter your choice: ")
    if reg_menu_choice.isdigit():
        reg_menu_choice=int(reg_menu_choice)

    return reg_menu_choice        