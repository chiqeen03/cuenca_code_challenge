class Board:
    def __init__(self, array):
        self.array = array
        self.n = len(array)

    def to_simple_string(self):
        simple_string = ""
        for i in range(0, self.n):
            for j in range(0, self.n):
                if self.array[i][j] == 1:
                    simple_string+=str(j)
        return simple_string
        
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