# Given an integer numRows, return the first numRows of Pascal's triangle.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for nele in range(1,numRows+1):
            temp = [None]*nele
            temp[0],temp[-1] = 1,1
            for i in range(1,len(temp) - 1):
                temp[i] = sum(ans[-1][i-1:i+1])
                # print("current temp:",temp)
            ans.append(temp)
        return ans