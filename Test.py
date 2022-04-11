ShopList = ['tomato', 'potato', 'fish']
Meat = []
Fish = []



print('please enter for options: ')

def Add_To_Category():
    list_selection = int(input('list would you like to add\n1) for Fish\n2) for Meat'))
    if list_selection == 1:
        list_update = str(input('enter item name:\n'))
        Meat.append(list_update)
    elif list_selection == 2:
        list_update = str(input('enter item name:\n'))
        Fish.append(list_update)
    else:
        print('invalid')

def addingitem():
    Item_name = input('Add item to shopping list:\n')
    ShopList.append(Item_name)





