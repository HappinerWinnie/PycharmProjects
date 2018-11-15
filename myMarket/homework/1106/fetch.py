def test():
    stuTuple  = (('001', 'zhangsan'),('002', 'lisi'),('003', 'wangwu'),)

    colTuple = (('ID',), ('NAME',))

    resultList = []
    for val in stuTuple:
        #dict = {}
        for column in colTuple:
            dict = {column:val}
        resultList.append(dict)

    return resultList

print(test())