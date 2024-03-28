board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 ==0 and i != 0:
            print("- - - - - - - - - - - - - -")
        
        for j in range (len(bo)):
            if j % 3 ==0 and j != 0:
                print(" | ", end ="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ",end="")
def isValid (bo,num,row,column):
    for i in range(len(bo)):
        if(bo[row][i] == num):
            return False
        if(bo[i][column] == num):
            return False
        if(bo[3*(row//3)+i//3][3*(column//3)+i%3]==num):
            return False
    return True


def solve(bo,row, column):
    n = len(bo)
    if(row == n):
        return True
    elif (column == n):
        return solve(bo,row+1,0)
    elif(bo[row][column] != 0):
        return solve(bo,row,column+1)
    else:
        for i in range(1,10):
            if(isValid(bo,i,row,column)):
                bo[row][column] = i
                if(solve(bo,row,column+1)):
                    return True
                else:
                    bo[row][column] = 0
        return False 

solve(board,0,0)
print_board(board)
            