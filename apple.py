import random

class Apple:
    def __init__(self, board_length) -> None:
        self.tag = 'X'
        
        self.board_length = board_length
        self.apple_poss = self.random_pos()

    def random_pos(self):
        apple_poss = []
        for _ in range(3):
            x = random.randint(1, self.board_length[0] - 1)
            y = random.randint(1, self.board_length[1] - 1)

            apple_poss.append([x, y])
        
        return apple_poss
