#implementiramo pygame v program
import pygame
from pygame.display import set_caption
import time
import random

#inicializiramo pygame komponento
pygame.init()

#nastavimo velikost igre in posodabljanje
dis_sirina = 800
dis_visina = 600
dis = pygame.display.set_mode((dis_sirina,dis_visina))
pygame.display.update()

#nastavimo naslov igre
pygame.display.set_caption('Snake game by Benonius')

#spremenljivke ki jih uporabimo v igri
white=(255,255,255)
yellow=(255,255,102)
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)

snake_block = 10
snake_hitrost = 15

ura = pygame.time.Clock()

font_style = pygame.font.SysFont(None,30)
tocke_font = pygame.font.SysFont(None,25)

def our_snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,black,[x[0],x[1], snake_block, snake_block])

def tocke(tocke):
    value = tocke_font.render("Tocke:" +str(tocke), True, green)
    dis.blit(value, [0,0])

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_sirina/6,dis_visina/3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = round(random.randrange(0,dis_sirina - snake_block) /10.0) * 10.0
    y1 = round(random.randrange(0,dis_visina - snake_block) /10.0) * 10.0

    x1_spr = 0
    y1_spr = 0

    snake_List = []
    Length_of_snake = 1

    hranax = round(random.randrange(0,dis_sirina - snake_block) /10.0) * 10.0
    hranay = round(random.randrange(0,dis_visina - snake_block) /10.0) * 10.0

    #potekanje igre
    while not game_over:
        while game_close == True:
            dis.fill(white)
            message("Izgubili ste. Pritisnite Q za zapreti ali C za igrati znova", red)
            tocke(Length_of_snake -1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        #gledanje pritisnjenih tipk
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_spr = -snake_block
                    y1_spr = 0
                elif event.key == pygame.K_RIGHT:
                    x1_spr = snake_block
                    y1_spr = 0
                elif event.key == pygame.K_UP:
                    x1_spr = 0
                    y1_spr = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_spr = 0
                    y1_spr = snake_block

        if x1 >= dis_sirina or x1 < 0 or y1 >= dis_visina or y1<0:
            game_close = True

        x1 += x1_spr
        y1 += y1_spr

        dis.fill(white)
        pygame.draw.rect(dis,blue,[hranax,hranay,snake_block,snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block,snake_List)
        
        pygame.display.update()

        if x1 == hranax and y1 == hranay:
            hranax = round(random.randrange(0,dis_sirina - snake_block) /10.0) * 10.0
            hranay = round(random.randrange(0,dis_visina - snake_block) /10.0) * 10.0
            Length_of_snake += 1
            print("Njami!")
            print("X: ",hranax, " Y: ",hranay)

        ura.tick(snake_hitrost)

    pygame.quit()
    quit()

gameLoop()