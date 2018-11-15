# 1
'''
1. A + B 问题
给出两个整数 a 和 b , 求他们的和。
'''
def aplusb(a, b):
    INT_RANGE = 0xFFFFFFFF
    while b != 0:
        a, b = a ^ b, (a & b) << 1
        a &= INT_RANGE
    return a if a >> 31 <= 0 else a ^ ~INT_RANGE
#print(aplusb(67248924724,47887))

def aplusb2(a, b):
    # write your code here
    while b:
        result = (a ^ b) & 0xffffffff
        carry = ((a & b) << 1) & 0xffffffff
        a = result
        b = carry
    if a <= 0x7fffffff:
        result = a
    else:
        result = ~(a ^ 0xffffffff)
    return result
print(aplusb2(67248924,47887))

#2
'''
设计一个算法，计算出n阶乘中尾部零的个数
O(logN)的时间复杂度
'''

def trailingZeros(n):
    # write your code here, try to do it without arithmetic operators.
    sum = 0
    while n != 0:
        n //= 5
        sum += n
    return sum
print(trailingZeros(50))

#3
'''
计算数字k在0到n中的出现的次数，k可能是0~9的一个值
例如n=12，k=1，在 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]，我们发现1出现了5次 (1, 10, 11, 12)
'''
def digitCounts(k, n):
    # write your code here
    result = 0
    for item in range(0, n + 1):
        count_tmp = str(item).count(str(k))
        result += count_tmp
    return result
print(digitCounts(1,100))



