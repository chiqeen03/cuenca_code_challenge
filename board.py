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