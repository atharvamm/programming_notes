# 119. Pascal's Triangle II
# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

def getRow(rowIndex):
    i = 0
    triangle = [None]*(rowIndex+1)
    while i < (rowIndex+1):
        num_eles = i+1
        triangle[i] = [1]*num_eles
        for ind in range(1,num_eles-1):
            triangle[i][ind] = triangle[i-1][ind - 1] + triangle[i-1][ind]
        i += 1
    return triangle[-1]

def getRow2(rowIndex):
    temp = [1]
    pascal = [1]
    while len(pascal) < rowIndex + 1:
        temp.append(0)
        pascal.insert(0,0)

        for i in range(len(pascal)):
            t = pascal[i] + temp[i]
            temp[i],pascal[i] = t,t
    return pascal

def getRow3(rowIndex):
    n = rowIndex + 1
    pascal = [1]*n

    for rowSize in range(3,n+1):
        middle = rowSize // 2
        even = rowSize%2 == 0
        if even: middle -= 1

        for index in range(middle,0,-1):
            pascal[index] = pascal[index] + pascal[index - 1]

        if even:
            for diff in range(1,rowSize - middle - 1):
                pascal[middle + diff] = pascal[middle - diff + 1]
        else:
            for diff in range(1,rowSize - middle - 1):
                pascal[middle + diff] = pascal[middle - diff]
    return pascal


from time import time
for index in [0,1,2,4,10,1000,2000]:
    start1 = time()
    op1 = getRow(index)
    end1 = time()

    start2 = time()
    op2 = getRow2(index)
    end2 = time()

    start3 = time()
    op3 = getRow2(index)
    end3 = time()

    print("Time_1:",end1 - start1,end = " ")
    print("Time_2:",end2 - start2,end = " ")
    print("Time_3:",end3 - start3,end = " ")
    print("Correct:",op1 == op2, op1 == op3)
