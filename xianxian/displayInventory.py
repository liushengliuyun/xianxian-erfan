"""定义一个函数,并按照要求打印字典中的相关信息,"""
i={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(inventory):
    print('Inventory:')
    a=0
    for k,v in inventory.items():
       print(v,k)   #变量拼接
       a=a+int(v)
    print('Total number of items:'+str(a)+'.')

displayInventory(i)   #函数的使用


addedI=['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def addToInventory(inventory,addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item]=inventory[item]+1
        else:
            inventory[item]=1
    return inventory
addToInventory(i,addedI)
displayInventory(i)