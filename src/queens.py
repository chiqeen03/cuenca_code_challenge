from board import Board

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
def solve(array, start_at, n, board_list):
    # base case
    if (start_at == n):
        arr = copy_array(array)
        # add to the global list the possible solution stored in a Board object
        board_list.append(Board(arr))
        return True
    
    #runs through each row of the column we are at (y)
    for i in range(n): 
        if(is_safe(array, i, start_at)):
            # we set the value to 1 to work with it later
            array[i][start_at] = 1
            # recursive call
            solve(array, start_at+1, n, board_list)
            # when we finish the recursive call we set the value to 0 again
            array[i][start_at] = 0
    return True

def get_all_possible_solutions(n):
    # list where we save all of the possible boards
    board_list = []

    # this array is the one we will use to store the different positions
    aux_array = empty_array(n)

    solve(aux_array, 0, n, board_list)

    return board_list
