from apple import Apple
from game import SnakeGame
from snake import Snake

ROW = 20
COL = 50

snake = Snake()
apple = Apple([ROW, COL])
game = SnakeGame(snake, apple, ROW, COL)



game.update()
