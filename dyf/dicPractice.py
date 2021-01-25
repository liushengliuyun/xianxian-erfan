m_dic = {'rope': 1,
         'torch': 6,
         'gold coin': 42,
         'dagger': 1,
         'arrow': 12}


def displayInventory(a_dic):
    print("Inventory:")
    sum = 0
    for k, v in a_dic.items():
        sum = sum + v
        print(k + " " + str(v))
    print("Total number of items :" + str(sum))


# displayInventory(m_dic)

testList = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def addToInventory(inventory, addedItems):
    for i, v in enumerate(addedItems):
        # if v in inventory.keys():
        #     inventory[v] = inventory[v] + 1
        # else :
        #     inventory[v] = 1

        # 简化写法, 和上面意思一样
        inventory[v] = v in inventory.keys() and inventory[v] + 1 or 1

    return inventory


displayInventory(addToInventory(m_dic, testList))
