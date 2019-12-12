# prints a simple interface where user can see the board (0 = no queen, 1 = queen)
def print_array(array):
    nm = "    "
    for i in range(n):
        nm += str(i) + " "
    print (nm)

    line = "   -"
    for i in range(n):
        if(i != n-1):
            line += "--"
        else:
            line += "-"
    print(line)

    for i in range(n):
        rw = str(i) + " | "
        if n >= 10 and i <= 9:
            rw = str(i) + "  | "
        for j in range(n):
            rw += str(array[i][j]) + " "
        print (rw)

    print("")

# returns a list with the even numbers from 0 to n
def get_evens(n):
    evens = []
    for i in range(n):
        if i % 2 == 0:
            evens.append(i)
    return evens
# returns a list with the odd numbers from 0 to n
def get_odds(n):
    odds = []
    for i in range(n):
        if i % 2 == 1:
            odds.append(i)
    return odds

# returns an array filled with "0"
def empty_array(n):
    return [[0] * n for i in range(n)]

# follows the method described in wikipedia to break the problem through brute force
def brute_force_list(n):
    if (n % 6 == 2):
        even_list = get_evens(n)
        # swaps 0 and 1
        even_list[0], even_list[1] = even_list[1], even_list[0]
        # sends 2 to last position
        even_list.append(even_list.pop(2))
        return get_odds(n) + even_list
    elif (n % 6 == 3):
        odd_list = get_odds(n)
        # sends 0 to last position
        odd_list.append(odd_list.pop(0))
        even_list = get_evens(n)
        # sends 0 and 1 to last position
        even_list.append(even_list.pop(0))
        even_list.append(even_list.pop(0))
        return odd_list + even_list
    return get_odds(n) + get_evens(n)

n = 8
board = empty_array(n)
print_array(board)

indexes = brute_force_list(n)

for i in range(n):
    board[i][indexes[i]] = 1

print_array(board)
