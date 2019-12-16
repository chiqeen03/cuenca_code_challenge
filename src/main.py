from board import Board
from constants import (output_route)

def clear_output_file():
    f = open(output_route, "w")
    f.write("")
    f.close()

def write_to_file(str):
    f = open(output_route, "a")
    f.write(str)
    f.close()

def copy_array(array):
    return [[array[x][y] for y in range(len(array[0]))] for x in range(len(array))]

def empty_array(n):
    return [[0] * n for i in range(n)]

# checks if there are dangerous queens previously placed in the board
def is_safe(array, x, y):
    n = len(array)
    # checks if there are queens at the row of the position
    for i in range(n):
        if array[x][i]:
            return False

    # checks if there are queens at the col of the position
    for i in range(n):
        if array[i][y]:
            return False

    # checks right-up diagonal (/)
    i = x
    j = y
    while i >= 0 and j < n:
        if array[i][j]:
            return False
        i -= 1
        j += 1

    # checks right-down diagonal (\)
    i = x
    j = y
    while i < n and j < n:
        if array[i][j]:
            return False
        i += 1
        j += 1

    # checks left-up diagonal (\)
    i = x
    j = y
    while i >= 0 and j >= 0:
        if array[i][j]:
            return False
        i -= 1
        j -= 1

    # checks left-down diagonal (/)
    i = x
    j = y
    while i < n and j >= 0:
        if array[i][j]:
            return False
        i += 1
        j -= 1

    return True

# recursive method to solve the algorithm
    # This method is inspired in a homework made by myself (Manuel Avalos) and
    # my teammate Diogo Burnay for the Intelligent Systems class. The assignment
    # consisted in solving this same problem but using unity as a graphical
    # interface. This algorithm was mainly based in the explanations we found 
    # on youtube and on several websites, and in this instance I am simplifying 
    # how the algorithm works, and also, I am using a much simpler graphical 
    # interface to represent how the queens are viewed
def solve(y):
    # base case
    if (y == n):
        global board_list
        arr = copy_array(aux_array)
        # add to the global list the possible solution stored in a Board object
        board_list.append(Board(arr))
        global solutions
        # increase the count of solutions
        solutions += 1
        return True
    
    #runs through each row of the column we are at (y)
    for i in range(n): 
        if(is_safe(aux_array, i, y)):
            # we set the value to 1 to work with it later
            aux_array[i][y] = 1
            # recursive call
            solve(y+1)
            # when we finish the recursive call we set the value to 0 again
            aux_array[i][y] = 0
    return True


n = 8

# this array is the one we will use to store the different positions
aux_array = empty_array(n)

# list where we save all of the possible boards
board_list = []
solutions = 0

solve(0)

print(f"solutions: {solutions}")
for board in board_list:
    board.print_array()

clear_output_file()
write_to_file("Hello World")