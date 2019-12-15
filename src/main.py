from board import Board

def empty_array(n):
    return [[0] * n for i in range(n)]

# checks if there are dangerous queens previously placed in the board
def is_safe(array, x, y):
    n = len(array)
    # checks if there are queens at the row of the position
    for i in range(n):
        if array[x][i]:
            print(f"(-) there is a queen at: {x}, {i}")
            return False

    # checks if there are queens at the col of the position
    for i in range(n):
        if array[i][y]:
            print(f"(|) there is a queen at: {i}, {y}")
            return False

    # checks right-up diagonal (/)
    i = x
    j = y
    while i >= 0 and j < n:
        if array[i][j]:
            print(f"(ru/)there is a queen at: {i}, {j}")
            return False
        i -= 1
        j += 1

    # checks right-down diagonal (\)
    i = x
    j = y
    while i < n and j < n:
        if array[i][j]:
            print(f"(rd\) there is a queen at: {i}, {j}")
            return False
        i += 1
        j += 1

    # checks left-up diagonal (\)
    i = x
    j = y
    while i >= 0 and j >= 0:
        if array[i][j]:
            print(f"(lu\) there is a queen at: {i}, {j}")
            return False
        i -= 1
        j -= 1

    # checks left-down diagonal (/)
    i = x
    j = y
    while i < n and j >= 0:
        if array[i][j]:
            print(f"(ld/) there is a queen at: {i}, {j}")
            return False
        i += 1
        j -= 1

    return True

# recursive method to solve the algorithm
def solve(y):
    pass

n = 4
board = Board(n)

# this array is the one we will use to store the different solutions
aux_array = empty_array(n)