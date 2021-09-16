from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')
x = 400
y = 90
sinx = 0
cosx = 0
change_mode = 0
count=0;
while True:
    if change_mode == 0:
        if count==0:
            while x<800:
                clear_canvas_now()
                grass.draw_now(400,50)
                character.draw_now(x, y)
                x+=2
                delay(0.01)
                if x>=800:
                    count = 1                    

        elif count==1:
            while y < 600:
                clear_canvas_now()
                grass.draw_now(400, 50)
                character.draw_now(x, y)
                y+=2
                delay(0.01)
                if y >= 600:
                    count =2
        elif count==2:
            while x > 0:
                clear_canvas_now()
                grass.draw_now(400, 50)
                character.draw_now(x,y)
                x-=2
                delay(0.01)
                if x <= 0:
                    count=3
        elif count == 3:
             while y > 90:
                clear_canvas_now()
                grass.draw_now(400,50)
                character.draw_now(x,y)
                y-=2
                delay(0.01)
                if  y <= 90:
                    count=0            
close_canvas()
