from services.service import *

class UI:
    def __init__(self):
        self.__board = Board()
        self.__service = Service(self.__board)


    def run_ui(self):
        print(self.__board)
        direction = "up"
        while True:
            try:
                user_input = input("Enter command: ")
                command = user_input.split(" ")
                if command[0] == "move":
                    if command[1] == ";":
                        steps = 1
                    else: steps = int(command[1])
                    self.__service.move(steps, direction)
                elif command[0] == "up" and direction == "down":
                    print("You cannot go 180 degrees!")
                elif command[0] == "up":
                    direction = "up"
                    self.__service.change_direction(direction)
                elif command[0] == "down" and direction == "up":
                    print("You cannot go 180 degrees!")
                elif command[0] == "down":
                    direction = "down"
                    self.__service.change_direction(direction)
                elif command[0] == "left" and direction == "right":
                    print("You cannot go 180 degrees!")
                elif command[0] == "left":
                    direction = "left"
                    self.__service.change_direction(direction)
                elif command[0] == "right" and direction == "left":
                    print("You cannot go 180 degrees!")
                elif command[0] == "right":
                    direction = "right"
                    self.__service.change_direction(direction)

            except ValueError as ve:
                if str(ve) == "Game is over! You lost!":
                    print("Game is over! You lost!")
                    exit()
                else: print(ve)

            print(self.__board)
