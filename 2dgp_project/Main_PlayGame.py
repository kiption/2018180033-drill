from pico2d import *
import random
from CharacterStaus import state
from Player_Mario import characterMario
import title_show
import game_framework

name = "Main_play"

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        if event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
            if (player.move_dir == 1):
                player.is_move = False
                player.state = state.Mario_Idle
        if event.type == SDL_KEYUP and event.key == SDLK_LEFT:
            if(player.move_dir == -1):
                player.is_move = False
                player.state = state.Mario_Idle
        if event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            player.state = state.Mario_Move

            player.is_move = True
            player.dirction = 1
            player.move_dir = 1
        if event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            player.state = state.Mario_Move
            player.is_move = True
            player.dirction = 2
            player.move_dir = -1
        if event.type == SDL_KEYDOWN and event.key == SDLK_c:
            player.state = state.S_jump
            #player.jump_charge = True
            #player.jump_on = True

        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_show)

        if event.type == SDL_KEYUP and event.key == SDLK_c:
            #player.jump_charge = False
            pass


def enter():

    global player
    global Ui
    global stage1_Bk
    global Platform
    global block
    global blocks
    global Grounds
    player = characterMario()
    #stage1_Bk = C_Stage1_Bk()
    #Ui =C_UI_()
    #platform_list=['random',900,300,'random',1500,300]

    #Platform =[Block('random',200,200),Block('brick',500,200)]
    #Grounds =[Ground(1104)]



def exit():
    global player , random_b ,stage1_Bk,Grounds,Platform
    del (player)
    del (Platform)
    del (Grounds)
    del (stage1_Bk)

def update():

    #for block in Platform:
    #    block.update(player.scroll_x)
    #for ground in Grounds:
    #    ground.update(player.scroll_x)
    #player.update()

    #stage1_Bk.update(player.scroll_x)

    #Ui.update(0,0,0)
    pass


def draw():
    clear_canvas()
    #stage1_Bk.draw()
    player.draw()
    #for block in Platform:
    #    block.draw()
    #for ground in Grounds:
    #    ground.draw()
    #Ui.draw()
    update_canvas()
    delay(0.03)