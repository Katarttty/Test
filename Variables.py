import os


ShopList = []



def addingitem():
    Item_name = input('Add item to List:\n ').capitalize()
    ShopList.append(Item_name)

addingitem()

while True:
    NewItem_request = input('would you like to add a new item\n [Y/N] ')
    if "y" in NewItem_request or "Y" in NewItem_request:
        print('okay')
        addingitem()
    elif "N" in NewItem_request or "n" in NewItem_request:
        ShopList.sort(key=str.lower)
        print('okay here is you list', *ShopList, sep='\n')
        print('you have', len(ShopList), 'items in your list')
        FileName = open(input("Enter Filename: ", ".txt"), 'w')
        for ShoplistFile in ShopList:
            FileName.write(ShoplistFile + "\n")
        FileName.close()
        break
    else:
        print('invalid')