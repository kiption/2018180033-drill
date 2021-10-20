import random
import json
import os

from pico2d import *
#import character_moves
#import title_state

name = "world1"
World_WIDTH, World_HEIGHT = 1048, 440

def ScreenEvent():
    events = get_events()
    for event in events:
        #if event.type == SDL_QUIT:
        #    game_framework.quit()
        #elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
        #    game_framework.change_state(title_state)
        pass

def handle_events():
    global running
    global x,y
    global y2
    global dir
    global m_x
    global turn
    global jump
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                turn = 2
                dir+=3
                m_x-=20
            elif event.key == SDLK_LEFT:
                turn = 0
                dir-=3
                m_x +=20
            elif event.key == SDLK_SPACE:
                jump = y
                y2 = y+50
                for i in range(0,100+1,5):
                    t=i/100
                    y =(1-t)*jump+t*y2
                delay(0.0005)
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type ==SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                turn=2
                dir -= 3
                m_x -= 20
            elif event.key == SDLK_LEFT:
                turn = 0
                dir += 3
                m_x += 20
            elif event.key == SDLK_SPACE:
                jump = y
                y2 = y - 50
                for i in range(0,100+1,1):
                    t=i/100
                    y =(1-t)*jump+t*y2
                delay(0.0005)
m_x = World_WIDTH
open_canvas(World_WIDTH, 600)
stage = load_image('Stage 1-1.png')
character1 = load_image('MM.png')
character2 = load_image('MM2.png')
running = True
x, y = World_WIDTH//2,90
y2=140
jump=0
dir = 0
frame1 = 0
frame2 = 0
turn = 0

while running:
    clear_canvas()
    stage.clip_draw(0, 100 * 1, 3447, 800, m_x, 275)
    if turn ==0:
        character1.clip_draw(frame1 * 26, dir, 25, 55, x, y)
        frame1 = (frame1 + 1) % 5
    if turn==2:
        character2.clip_draw(frame2 * 26, dir, 25, 55, x, y)
        frame2 = (1+frame2) % 5
    update_canvas()

    handle_events()
    delay(0.1)
    x += dir * 2



close_canvas()