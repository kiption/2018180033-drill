from pico2d import *
import random

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

class Boy:
    def __init__(self):
        self.x, self.y =  random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)

class ball1:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 700
        self.image = load_image('ball21x21.png')
    def update(self):
        if self.y == 30:
            self.y = 30
        else:
            self.y -= 10
    def draw(self):
        self.image.draw(self.x, self.y)

class ball2:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 700
        self.image = load_image('ball41x41.png')
    def update(self):
        if self.y == 30:
            self.y = 30
        else:
            self.y -= 10
    def draw(self):
        self.image.draw(self.x, self.y)

running = True

TotalBall1 = [ball1() for k in range(11)]
TotalBall2 = [ball2() for t in range(11)]

team = [Boy() for i in range(11)]

while running:
    handle_events()
    for Boy in team:
        Boy.update()
        Boy.draw()
    for ball1 in TotalBall1:
        ball1.update()
        ball1.draw()
    for ball2 in TotalBall2:
        ball2.update()
        ball2.draw()

    clear_canvas()
    Grass.draw()
    update_canvas()
    delay(0.05)

close_canvas()
# game main loop code


# finalization code