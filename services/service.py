from domain.domain import *
import random

class Service:
    def __init__(self, board):
        self.__board = board
        self.generate_snake()
        self.generate_random_apples()

    def generate_snake(self):
        size = self.__board.get_size()
        self.__board.set_square(size // 2 , size // 2, "+")
        self.__board.set_square(size // 2 - 1, size // 2, "*")
        self.__board.set_square(size // 2 + 1, size // 2, "+")
    def generate_random_apples(self):
        apples = self.__board.get_apples()
        size = self.__board.get_size()
        while apples > 0:
            i = random.randint(0, size - 1)
            j = random.randint(0, size - 1)
            if (self.__board.get_square(i, j) == "" and self.__board.get_square(i + 1, j) != "a" and self.__board.get_square(i, j + 1) != "a"
                and self.__board.get_square(i, j - 1) != "a" and self.__board.get_square(i - 1, j) != "a"):
                self.__board.set_square(i, j, "a")
                apples -= 1

    def change_direction(self, direction):

        size = self.__board.get_size()
        pos_i = 0
        pos_j = 0
        counter = 0
        for i in range(size):
            for j in range(size):
                if self.__board.get_square(i, j) == "*":
                    pos_i = i
                    pos_j = j

        if direction == "up":
            posi2 = 0
            posj2 = 0
            for i in range(size):
                for j in range(size):
                    if self.__board.get_square(i, j) == "+":
                        counter += 1
                        if counter == 2:
                            posi2 = i
                            posj2 = j
                            self.__board.set_square(i, j, "")

            self.__board.set_square(pos_i - 1, pos_j, "*")
            self.__board.set_square(pos_i, pos_j, "+")
            self.__board.set_square(posi2, posj2, "")

        if direction == "down":
            posi2 = 0
            posj2 = 0
            for i in range(size):
                for j in range(size):
                    if self.__board.get_square(i, j) == "+":
                        counter += 1
                        if counter == 2:
                            posi2 = i
                            posj2 = j
                            self.__board.set_square(i, j, "")

            self.__board.set_square(pos_i + 1, pos_j, "*")
            self.__board.set_square(pos_i, pos_j, "+")
            self.__board.set_square(posi2, posj2, "")

        if direction == "left":
            posi2 = 0
            posj2 = 0
            for i in range(size):
                for j in range(size):
                    if self.__board.get_square(i, j) == "+":
                        counter += 1
                        if counter == 2:
                            posi2 = i
                            posj2 = j
                            self.__board.set_square(i, j, "")

            self.__board.set_square(pos_i, pos_j - 1, "*")
            self.__board.set_square(pos_i, pos_j, "+")
            self.__board.set_square(posi2, posj2, "")

        elif direction == "right":
            posi2 = 0
            posj2 = 0
            for i in range(size):
                for j in range(size):
                    if self.__board.get_square(i, j) == "+":
                        counter += 1
                        if counter == 2:
                            posi2 = i
                            posj2 = j
                            self.__board.set_square(i, j, "")

            self.__board.set_square(pos_i, pos_j + 1, "*")
            self.__board.set_square(pos_i, pos_j, "+")
            self.__board.set_square(posi2, posj2, "")

    def move(self, steps, direction):
        size = self.__board.get_size()
        pos_i = 0
        pos_j = 0
        counter = 0
        for i in range(size):
            for j in range(size):
                if self.__board.get_square(i, j) == "*":
                    pos_i = i
                    pos_j = j

        if direction == "up":
            for i in range(size):
                for j in range(size):
                    if self.__board.get_square(i, j) == "+":
                        self.__board.set_square(i, j, "")
                        counter += 1

            self.__board.set_square(pos_i - steps, pos_j, "*")
            self.__board.set_square(pos_i, pos_j, "")
            pos_i = pos_i - steps

            for i in range(1, counter + 1):
                self.__board.set_square(pos_i + i, pos_j, "+")

        elif direction == "down":
            counter = 0
            for i in range(size):
                for j in range(size):
                    if self.__board.get_square(i, j) == "+":
                        self.__board.set_square(i, j, "")
                        counter += 1
            self.__board.set_square(pos_i + steps, pos_j, "*")
            self.__board.set_square(pos_i, pos_j, "")
            pos_i = pos_i + steps

            for i in range(1, counter + 1):
                self.__board.set_square(pos_i - i, pos_j, "+")

        elif direction == "left":
            for i in range(size):
                for j in range(size):
                    if self.__board.get_square(i, j) == "+":
                        self.__board.set_square(i, j, "")
                        counter += 1
            self.__board.set_square(pos_i, pos_j - steps, "*")
            self.__board.set_square(pos_i, pos_j, "")

            pos_j = pos_j - steps

            for i in range(1, counter + 1):
                self.__board.set_square(pos_i, pos_j + i, "+")
        elif direction == "right":
            for i in range(size):
                for j in range(size):
                    if self.__board.get_square(i, j) == "+":
                        self.__board.set_square(i, j, "")
                        counter += 1
            self.__board.set_square(pos_i, pos_j + steps, "*")
            self.__board.set_square(pos_i, pos_j, "")

            pos_j = pos_j + steps

            for i in range(1, counter + 1):
                self.__board.set_square(pos_i, pos_j - i, "+")



