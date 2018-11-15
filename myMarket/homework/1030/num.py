list=[1,2,3,4]
i=0
for x in range(1,len(list)+1):
    for y in range(1, len(list) + 1):
        for z in range(1, len(list) + 1):
            if x!=y and y!=z and x!=z:
                i += 1
                if i % 4:
                    print("%d%d%d" % (x, y, z), end=" | ")
                else:
                    print("%d%d%d" % (x, y, z))
