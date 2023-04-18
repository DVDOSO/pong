# by david

import pygame
pygame.init()
main = pygame.display.set_mode((650, 450))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

p1PaddleX = 30
p1PaddleY = 0
p2PaddleX = 610
p2PaddleY = 0
circleX = 100
circleY = 100
xv = 10
yv = 10

while True:
  pygame.event.clear()
  main.fill(WHITE)
  
  keys = pygame.key.get_pressed()

  paddle1Collision = pygame.Rect((p1PaddleX, p1PaddleY, 10, 150))
  pygame.draw.rect(main, BLACK, paddle1Collision)

  paddle2Collision = pygame.Rect((p2PaddleX, p2PaddleY, 10, 150))
  pygame.draw.rect(main, BLACK, paddle2Collision)

  if keys[pygame.K_w] and p1PaddleY >= 0:
    p1PaddleY -= 10
  if keys[pygame.K_s] and p1PaddleY <= 300:
    p1PaddleY += 10
  if keys[pygame.K_UP] and p2PaddleY >= 0:
    p2PaddleY -= 10
  if keys[pygame.K_DOWN] and p2PaddleY <= 300:
    p2PaddleY += 10

  circleCollision = pygame.Rect((circleX, circleY, 20, 20))
  pygame.draw.circle(main, GREEN, (circleX, circleY), 20)

  circleX += xv
  circleY += yv

  if circleY <= 0 or circleY > 430:
    yv *= -1
  if circleX <= 0 or circleX > 630:
    circleX = 100
    circleY = 100
  if pygame.Rect.colliderect(circleCollision, paddle1Collision):
    circleX = p1PaddleX + 20
    xv *= -1
    
  if pygame.Rect.colliderect(circleCollision, paddle2Collision):
    circleX = p2PaddleX - 20
    xv *= -1
  
  pygame.time.delay(40)
  pygame.display.update()