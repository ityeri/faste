import pygame
import math

pygame.init()
screen = pygame.display.set_mode((500, 500))

running = True
while running:
    screen.fill((30, 30, 30))

    # (x, y, width, height) = (100, 100, 200, 100)의 사각형을 기준으로 호 그리기
    rect = (0, 0, 500, 500)  # 타원을 그릴 사각형 (x, y, width, height)
    
    # 호 그리기: 0 라디안(0도)부터 pi 라디안(180도)까지
    pygame.draw.arc(screen, (255, 0, 0), rect, 0, math.pi, 5)

    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
