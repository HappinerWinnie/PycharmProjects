list=[1,2,3,4]
for x in range(1,len(list)+1):
    for y in range(1, len(list) + 1):
        for z in range(1, len(list) + 1):
            if x!=y and y!=z and x!=z:
                print('%d|%d|%d' %(x,y,z))