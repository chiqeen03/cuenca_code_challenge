from board import Board

n = 4
board = Board(n)
board.print_array()

# board.place_queen_at(2,0)
# board.place_queen_at(0,2)
board.place_queen_at(0,0)

board.print_array()

# print(board.is_safe(2, 3))
# print(board.is_safe(3, 2))
# print(board.is_safe(1, 3))
print(board.is_safe(3, 3))