def search_menu_view():
    print("\nplease select one of the options to searh with")
    print("1. From Name")
    print("2. From Address")
    print("3. From Contact")
    print("4. View All Records")
    print("5. Go Back")

    search_menu_choice=input("Please Enter Your Choice: ")
    if search_menu_choice.isdigit():
        search_menu_choice=int(search_menu_choice)

    return search_menu_choice    