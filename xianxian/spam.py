# 将列表信息返回为字符串
family_members = ['caoshujun', 'lishiqing', 'caomaoxia', 'daiyifan', 'tuanzi']
print(','.join(family_members[:-1]) + ' and ' + family_members[-1])
# 利用外层变量,然后使用拼接的方法将for循环中的变量保存下来
a = ''
for fm in family_members[:-1]:
    if a == '':
        a = fm
    else:
        a = a + ',' + fm
a = a + ' and ' + family_members[-1]

print(a)


