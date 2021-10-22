from pico2d import *
from CharacterStaus import state
from CharacterStaus import Mario_Growth
import time

class characterMario():
    def __init__(self):
        self.x = 300
        self.y = 100
        self.frame = 0
        self.direction = 0
        self.image = load_image('mario_growth.png')
        self.jump_height = 0
        self.move_dir = 1
        self.is_move = False
        self.jump_on = False
        self.size_x = 32
        self.size_y = 32
        self.is_land = True
        self.First_frame = True
        self.M_state = Mario_Growth.mario
        self.Drop = False
        self.time_cnt = 0
        self.accel = 0
        self.state = state.Mario_Idle
        self.gravity = 9.8

    def draw(self):
        self.image.clip_draw(32*self.frame+1, 32*self.direction, 32, 32, self.x, self.y)




    def update(self):
        self.update_state()
        self.move()
        self.jump()


    def move(self):

            if (self.is_move):
                if self.x < 650 - self.move_dir * self.accel and self.x >= 50 - self.move_dir * self.accel:
                    self.x += self.move_dir * self.accel

                elif self.x >= 650 - self.move_dir * self.accel:
                    #if (self.scroll_x < 7150):
                    #    self.scroll_x += self.move_dir * self.accel
                    pass
                if self.accel < 10.0:
                    self.accel += 0.5
                self.priv_state = state.Mario_Move


    def update_state(self):
        self.Flame_Change_End =time.time()
        if self.is_move and self.jump_on == False:
            self.state = state.Mario_Move
        if self.is_move and self.jump_on == True:
            self.state = state.Mario_Jump


    def jump(self):
        #if(self.is_Coll==False): self.drop=True

        if self.jump_on:

            self.jump_accel += 0.2
            vel = self.jump_accel - self.gravity * (self.jump_accel ** 2) * 0.5

            #if self.jump_charge:
            #    self.jump_power += 0.6
            if (vel < 0):self.Drop = True;

            self.y+=vel

            #if(self.is_Coll and self.Drop):
            #    self.y = self.Coll_y + self.size_y/2
            #    self.jump_on = False
            #    self.Drop = False

             #   print(self.size_y)
             #   self.jump_accel = 0
             #   self.jump_power = 10
             #   self.state = state.S_idle
        #if self.Drop and self.jump_on==False:

            self.jump_accel +=0.2
            self.y -= 5 * self.gravity * self.jump_accel *0.5
        #    if (self.y - 5 * self.gravity * self.jump_accel *0.5 <= self.Coll_y):
        #        self.y = self.Coll_y + self.size_y / 2
         #       self.jump_on = False
          #      self.Drop = False

           #     self.jump_accel = 0

            #    self.jump_power = 10
            #    self.state = state.S_idle