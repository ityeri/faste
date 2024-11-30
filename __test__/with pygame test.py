from imghdr import tests
import os
import pygame
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import __init__ as faste


pygame.init()

testScene = faste.Scene()

testRect1 = faste.element.UIRect("1", (0, 0, 255), (10, 10, 100, 100),
                              borderRadius=20)

testRect2 = faste.element.UIRect("2", (0, 255, 0), (11, 11, 100, 100),
                              borderRadius=20)

testScene.addElement(testRect1)
testScene.addElement(testRect2)

testScene.setOrder("1", 0)


# 파이게임 설정
screen = pygame.display.set_mode((500, 500))
clk = pygame.Clock()
fps = 60
dt = 10
on = True


while on:
    dt = clk.tick(fps)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False

    
    screen.fill((0,0,0))


    testScene.draw(screen)

    pygame.display.flip()