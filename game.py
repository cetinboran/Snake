import threading
import fpstimer
import os
import time

class SnakeGame:
    def __init__(self, snake) -> None:
        self.board = [[" " for _ in range(50)] for _ in range(20)]
        self.game_time = fpstimer.FPSTimer(10)
        self.snake = snake

    def draw_board(self):
        for i, row in enumerate(self.board):
            output = ""
            for j, value in enumerate(row):
                output += value

            print(output)

    def config_board(self):
        for i, row in enumerate(self.board):
            for j, value in enumerate(row):
                if i == 0 or i == len(self.board) - 1 or j == 0 or j == len(self.board[0]) - 1:
                    self.board[i][j] = "#"
                elif [i, j] == self.snake.pos:
                    self.board[i][j] = self.snake.tag
                elif [] != self.snake.pos:
                    self.board[i][j] = " "
                else:
                    self.board[i][j] = value

        self.draw_board()
        
    def collision(self):
        for i, row in enumerate(self.board):
            for j, value in enumerate(row):
                if value == "#":
                    if self.snake.pos == [i, j]:
                        self.snake.dead = True
                        return value

    def update_backend(self):
        pass


    def update(self):
        threading.Thread(target=self.snake.get_move,).start()
        while True:
            os.system("cls")

            self.config_board()

            self.snake.move()

            if self.collision() == "#":
                print("You Lost")
                break

            self.game_time.sleep()
            #time.sleep(.2)