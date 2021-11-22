from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global dir
    global ani
    global mouse_x, mouse_y
    events = get_events()
    for events in events:
        if events.type == SDL_QUIT:
            running = False
        elif events.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = events.x, 600 - 1 - events.y
            if(mouse_x > 400):
                dir = 1
                ani = 1
            elif (mouse_x <= 400):
                dir = 1
                ani = 0

            elif events.key == SDLK_ESCAPE:
                running= False;

def character_move():
    global x, y
    global mouse_x, mouse_y

    x = (1-0.05)*x+0.05*mouse_x
    y = (1-0.05)*y+0.05*mouse_y




open_canvas()
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')
hide_cursor()
running = True

frame = 0
dir = 0
ani = 3
x, y = 800 // 2, 600 // 2
mouse_x = 500
mouse_y = 600//2
hide_cursor()
while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 1*100, 100, 100, x, y)
    cursor.clip_draw(0, 0, 50, 52, mouse_x, mouse_y)
    update_canvas()
    character_move()
    handle_events()
    frame = (frame + 1) % 8

    delay(0.01)

close_canvas()