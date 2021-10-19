from pico2d import *

class characterMario():
    def __init__(self):
        self.x = 300
        self.y = 100
        self.frame = 0
        self.direction = 0

    def draw(self):
        self.image.clip_draw(32*self.frame, 32*self.direction, 32, 32, self.x, self.y)


