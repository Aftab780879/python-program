def search_ingredients(coffee):
    

    ingredients_search=input("please enter the ingredients from which you want to search(use alphabets only): ")  
    for item in coffee:
        ingredient_list=[ingredient.lower() for ingredient in item["ingredients"]]
        if ingredients_search.lower() in ingredient_list:
            print(item)
            break
    else:
            print("NO DATA FOUND")