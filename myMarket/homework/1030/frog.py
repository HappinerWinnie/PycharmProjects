def dump(day,night,height):
    sum = 0
    days = 1
    while sum < height:
        sum += day
        if sum < height:
            sum -= night
            days += 1
    return days
print(dump(3,1,11))