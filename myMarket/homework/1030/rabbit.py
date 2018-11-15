r1 = 1
r2 = 1
sum = 0
for i in range(1,13):
    if i <= 2:
        print('第%d个月兔子为%d对' %(i,r1))
    else:
        sum = r1 + r2
        r1 = r2
        r2 = sum
        print('第%d个月兔子为%d对' %(i,r2))