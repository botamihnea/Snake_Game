from texttable import Texttable

class Board:
    def __init__(self):
        size = int(self.get_size())
        self.__board = [["" for _ in range (size)] for _ in range(size)]


    def get_size(self):
        with open("input", "r") as file:
            for line in file:
                line.strip()

                if line == "":
                    continue

                line.split(" ")
                size = line[0]
        file.close()
        return int(size)

    def get_apples(self):
        with open("input", "r") as file:
            for line in file:
                line.strip()

                if line == "":
                    continue

                line = line.split(" ")
                apples = line[1]

        return int(apples)

    def get_square(self, i, j):
        size = int(self.get_size())
        if i < 0 or j < 0 or i > size - 1 or j > size - 1:
            return ""
        else:
            return self.__board[i][j]

    def set_square(self, i, j, symbol):
        if i < 0 or j < 0 or i > self.get_size() - 1 or j > self.get_size() - 1 and symbol == "*":
            raise ValueError("Game is over! You lost!")
        elif symbol == "*" and self.get_square(i, j) == "+":
            raise ValueError("Game is over! You lost")
        elif i < 0 or j < 0 or i > self.get_size() - 1 or j > self.get_size() - 1:
            raise ValueError("Invalid coordinates!")
        else:
            self.__board[i][j] = symbol


    def __str__(self):
        table = Texttable()
        size = self.get_size()
        for i in range(size):
            added_row = []
            for j in range(size):
                added_row.append(self.__board[i][j])

            table.add_row(added_row)

        return table.draw()
