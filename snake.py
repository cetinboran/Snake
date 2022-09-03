from pynput.keyboard import Key, Listener

class Snake:
    def __init__(self) -> None:
        self.tag = "O"

        self.speed_x = 1
        self.speed_y = 0
        self.pos = [2, 5]
        self.ex_pos = list()


        self.dead = False

        self.direction = [False, False, True, False]

    def move(self):
        self.pos[0] += self.speed_x
        self.pos[1] += self.speed_y



    def on_press(self, key):
        if key == Key.left and self.direction[0] != True:
                self.speed_x = 0
                self.speed_y = -1

                self.direction[1] = True
                self.direction[2] = self.direction[3] = False
        if key == Key.right and self.direction[1] != True:
                self.speed_x = 0
                self.speed_y = 1

                self.direction[0] = True
                self.direction[2] = self.direction[3] = False
        if key == Key.up and self.direction[2] != True:
                self.speed_x = -1
                self.speed_y = 0

                self.direction[3] = True
                self.direction[0] = self.direction[1] = False
        if key == Key.down and self.direction[3] != True:
                self.speed_x = 1
                self.speed_y = 0

                self.direction[2] = True
                self.direction[0] = self.direction[1] = False

        if self.dead == True: 
            return False

    def get_move(self):
        while not self.dead:
            with Listener(on_press=self.on_press) as listener:
                listener.join()
