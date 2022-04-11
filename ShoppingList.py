ShopList = []

def save_list():
    save_as_txt = input('Save list as .txt: [Y/N]\n')
    while True:
        if "y" in save_as_txt or "Y" in save_as_txt:
            Txt_file_name = input("enter name: ")
            FileName = open(Txt_file_name + ".txt", 'w')
            for ShoplistFile in ShopList:
                FileName.write(ShoplistFile + "\n")
            FileName.close()
            print('....txt file created....\nthank you for using\nKatarttty\'s shoping app')
            break
        elif "N" in save_as_txt or "n" in save_as_txt:
            print('Ending program')
            break
        else:
            print('invalid')

def adding_item():
    Item_name = input('Add item to List:\n').capitalize()
    while True:
        if Item_name not in ShopList:
            ShopList.append(Item_name)
            print('item added')
            break
        elif Item_name in ShopList:
            print('already added')
            break
        else:
            print('invalid')

adding_item()

while True:
    NewItem_request = input('would you like to add a new item\n [Y/N] ')
    if "y" in NewItem_request or "Y" in NewItem_request:
        print('okay')
        adding_item()
    elif "N" in NewItem_request or "n" in NewItem_request:
        print('okay here is you list', *ShopList, sep='\n')
        print('you have', len(ShopList), 'items in your shopping list')
        save_list()
        break
    else:
        print('invalid')