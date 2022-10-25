import sys
def MinCostPathI(matrix,mRows,nCols):
    dp = [[0 for i in range(nCols)] for j in range(mRows)]
    down = sys.maxsize
    right = sys.maxsize
    diagonal = sys.maxsize
    for i in range(mRows-1,-1,-1):
        for j in range(nCols-1,-1,-1):
            #print(i,j,matrix[i][j],end=' ')
            down = sys.maxsize
            right = sys.maxsize
            diagonal = sys.maxsize
            if i+1<mRows:
                down = dp[i+1][j]
                flag = True
            if j+1<nCols:
                right = dp[i][j+1]
                flag = True
            if i+1<mRows and j+1<nCols:
                diagonal = dp[i+1][j+1]
                flag = True
            if i == mRows-1 and j==nCols-1:
                dp[i][j] = matrix[i][j]
            else:
                dp[i][j] = matrix[i][j]+min(down,right,diagonal)
            #print(dp[i][j])
            
    print(dp)
    return dp[0][0]
        

def take2DInput() :
    li = [int(x) for x in input().split()]
    mRows = int(li[0])
    nCols = int(li[1])
    
    if mRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(mRows)]
    return mat, mRows, nCols


#main
mat, mRows, nCols = take2DInput()
print(MinCostPathI(mat, mRows, nCols))
