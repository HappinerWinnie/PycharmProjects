height = 100
cur_height = 0
sum = 0
for i in range(1,11):
    height = height / 2
    cur_height = height * 2 + cur_height
    sum = cur_height + 100 - height
    print('第%d次' %i)
    print('当前高度%f' %height)
    print('总共经过%f' %sum)

