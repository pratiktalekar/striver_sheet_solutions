def generate(self, numRows: int):
    ans = []   
    ans.append([1])
    if numRows == 1:
        return ans
    for i in range(2, numRows+1):
        nextArr = []
        prevArr = ans[i - 2]
        nextArr.append(1)
        for j in range(0, i - 2):
            nextArr.append(prevArr[j] + prevArr[j + 1])
        nextArr.append(1)
        ans.append(nextArr)
    
    return ans