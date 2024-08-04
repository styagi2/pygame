import pygame
from pygame.locals import *
import random

#initializing pygame 
pygame.init()
running = True

#dimensions 
size = width, height = (800,800) #sscreen size
road_width = int(width/1.6)
roadmark_width = int(width/80)

#lane defined

right_lane = width/2 + road_width/4
left_lane = width/2 - road_width/4

#set window size
screen = pygame.display.set_mode (size)

#set title of the window
pygame.display.set_caption("Tyagi Car Game")

#fill screen with color
screen.fill((60, 220,0))


#load images mycar 
car1 = pygame.image.load("mycar.png")
car1_loc = car1.get_rect()
car1_loc.center = right_lane, height*0.8

#load images otherCar 
car2 = pygame.image.load("othercar.png")
car2_loc = car2.get_rect()
car2_loc.center = left_lane, 0

#selected a variable for speed
counter = 0
speed = 1
score = 0
#keeping score 

#displaying score

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
font = pygame.font.Font('freesansbold.ttf', 32)

#game loop
while(running):

    counter += 1
    if counter == 2000:
        counter = 0
        speed += 0.25

    car2_loc = car2_loc.move([0, speed]) #[moving car from top to down y axis]
    if car2_loc[1] > height:
        score +=1
        #inserting random lane logic
        if random.randint(0,1) == 0:
            car2_loc.center = right_lane,0 #CHANGE car 2 to right lane
        else:
            car2_loc.center = left_lane,0  #CHANGE car 2 to left lane

    #end game / collision logic
    if car1_loc[0] == car2_loc[0] and car1_loc.top <= car2_loc.bottom:
        print("Final Score: %s" %score)
        print("gmae over")
        pygame.quit()


    for event in pygame.event.get():
        if event.type == QUIT:      #this is for exiting the game
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT] and car1_loc.center[0] > int(width/2):
                car1_loc = car1_loc.move([-int(road_width/2), 0])
        if event.type == KEYDOWN:
            if event.key in [K_d, K_RIGHT] and car1_loc.center[0] < int(width/2):
                car1_loc = car1_loc.move([int(road_width/2), 0])

    ####draw graphics#####

    #draw road
    pygame.draw.rect(
        screen, (50,50,50), 
        (width/2-road_width/2, 0,road_width, height)
    )

    #draw mid road markers
    pygame.draw.rect(
        screen, 
        (255,240,60),
        (width/2 -roadmark_width/2,0, roadmark_width,height)
    )

    #draw left side road markers
    pygame.draw.rect(
        screen, 
        (255,255,255),
        (width/2 -road_width/2 + roadmark_width*2, 0, roadmark_width,height)
    )

    #draw right side road markers
    pygame.draw.rect(
        screen, 
        (255,255,255),
        (road_width/2 + width/2 - roadmark_width*3,0, roadmark_width,height)
    )
    
    #display score
    text = font.render('Score:'+str(score), True, green, blue)
    textRect = text.get_rect()
    textRect.center = (60, 20)
    
    screen.blit(text, textRect)
    screen.blit(car1, car1_loc)
    screen.blit(car2, car2_loc)
    pygame.display.update()
pygame.quit()