family = {
    'father': 'caoshujun',
    'mother': 'lishiqing',
    'daughter': "caomaoxia",
    "boyfriend": 'daiyifan'}
print(family.keys())
print(family.items())
for member in family.keys():
    if member == 'daughter':
        print("I'm " + family[member] + '.')
    else:
        if member == 'mother':
            print('This is my ' + member + ', her name is ' + family[member])
        else:
            print('This is my ' + member + ', his name is ' + family[member])
