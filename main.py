import test


print('创建新的表格按1， 已有表格按2')
start = input()
print('输入表格名称')
table_name = input()
if start == '1':
    atable = test.Table()
    atable.create()
elif start == '2':
    pass

