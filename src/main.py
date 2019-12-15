from board import Board

n = 4
board = Board(n)
board.print_array()

board.place_queen_at(3,7)

board.print_array()