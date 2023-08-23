import pygame
import neat
import os
import time
import random


WIN_WIDTH= 600
WIN_HEGHT = 800

BIRD_IMG = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird1.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird2.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird3.png")))]
PIPE_IMG =[pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","pipe.png")))]
BASE_IMG =[pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","base.png")))]
BG_IMG =[pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bg.png")))]

class bird:
    IMGS = BIRD_IMG
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION = 5

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.tilt=0
        self.tick_count=0
        self.vel=0
        self.height=self.y
        self.img_count=0
        self.img = self.IMGS[0]
    
    def jump(self):
        self.vel= -10.5
        self.tick_count=0
        self.height = self.y

    def move(self):
        self.tick_count+=1

        d=self.vel*self.tick_count+1.5*self.tick_count**2

        if d >= 16:
            d=d/abs(d)*16


#https://www.youtube.com/watch?v=ps55secj7iU&list=PLzMcBGfZo4-lwGZWXz5Qgta_YNX3_vLS2&index=2








