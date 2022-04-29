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


def input_board():
    print("Enter the input sudoku")
    for i in range(9):
        row=input(f"Enter row {i}:")
        for j in range(9):
            val=int(row[j])
            board[i][j]=val

    print("Your input")
    print_board(board)
            





def solve(bo):
    find=find_empty(bo)
    if not find:
        return True
    else:
        row,col=find
        for i in range(1,10):
            if valid(bo,i,(row,col)):
                bo[row][col]=i

                if solve(bo):
                    return True
                bo[row][col]=0

        return False 




def valid(bo,num,pos):
    # value = bo[pos[0]][pos[1]] 
    row=pos[0]
    col=pos[1]
    for i in range(len(bo[0])):
        if bo[row][i]==num and col!=i:
            return False
    for j in range(len(bo)):
        if bo[i][col]==num and row!=i:
            return False
    
    box_x=col//3
    box_y=row//3

    for i in range(box_y*3,box_y*3+3):
        for j in range(box_x*3,box_x*3+3):
            if bo[i][j]==num and (i,j)!=pos:
                return False
    return True 




def print_board(bo):
    for i in range((len(bo))):
        if i%3==0 and i!=0:
            print("------------------------")
        for j in range((len(bo))):
            if j%3==0 and j!=0:
                print("|", end="")
            if j==8:
                print(bo[i][j])
            else:
                print(str(bo[i][j])+ " ",end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo)):
            if bo[i][j]==0:
                return (i,j)
    return None

# print_board(board) 
input_board()
solve(board)
print("Solved sudoku :")
print_board(board)
