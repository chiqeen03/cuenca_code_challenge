class Board:
    def __init__(self, array):
        self.array = array
        self.n = len(array)

    # returns an array filled with "0"
    def fill_empty_array(self):
        return [[0] * self.n for i in range(self.n)]

    # prints a simple interface where user can see the board (0 = no queen, 1 = queen)
    def print_array(self):
        n = self.n
        array = self.array
        
        nm = "  y "
        for i in range(n):
            nm += f"{i} "
        print (nm)

        line = "x  -"
        for i in range(n):
            if(i != n-1):
                line += "--"
            else:
                line += "-"
        print(line)

        for i in range(n):
            rw = f"{i} | "
            if n >= 10 and i <= 9:
                rw = f"{i}  | "
            for j in range(n):
                rw += f"{array[i][j]} "
            print (rw)

        print("")

    def to_string(self):
        n = self.n
        array = self.array
        array_to_string = ""

        nm = "  y "
        for i in range(n):
            nm += f"{i} "
        array_to_string+= f"{nm}\n"

        line = "x  -"
        for i in range(n):
            if(i != n-1):
                line += "--"
            else:
                line += "-"
        array_to_string += f"{line}\n"

        for i in range(n):
            rw = f"{i} | "
            if n >= 10 and i <= 9:
                rw = f"{i}  | "
            for j in range(n):
                rw += f"{array[i][j]} "
            array_to_string += f"{rw}\n"
        
        array_to_string += "\n"

        return array_to_string

    # writes a queen (1) at a certain position (x, y)
    def place_queen_at(self, x, y):
        if self.in_bounds(x, y):
            self.array[x][y] = 1

    # deletes a queen at a certain position (x, y)
    def delete_queen_at(self, x, y):
        if self.in_bounds(x, y):
            self.array[x][y] = 0

    # returns what value is at a certain position (x, y)
    def get_value_at(self, x, y):
        if self.in_bounds(x, y):
            return self.array[x][y]
        return -1

    # simple method to check if (x, y) is in bounds
    def in_bounds(self, x, y):
        if (x >= self.n or y >= self.n or x < 0 or y < 0):
            return False
        return True

    