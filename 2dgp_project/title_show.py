import game_framework
import Main_PlayGame
from pico2d import *


name = "main_title"
image = None


def enter():
    global image
    image = load_image('title.png')


def exit():
    global image
    del (image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(Main_PlayGame)


def draw():
    clear_canvas()
    image.draw(400, 300, 800, 600)
    update_canvas()