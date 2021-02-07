spam = {'color': 'red', 'age': 42}
# 以下方法输出的是类似列表的的dict_keys数据类型
print(spam.keys())
# 使用list函数将以上输出转换为列表
print(list(spam.keys()))



import pprint  #导入pprint类

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}  #count是一个空字典
for character in message:
    count.setdefault(character, 0)  #对message中的字符进行计数,并默认数值为0
count[character] = count[character] + 1

pprint.pprint(count)  #类名+函数名
