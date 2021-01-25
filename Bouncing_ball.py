import pygame

pygame.init()
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption("Bouncing ball")
ball=pygame.image.load("Resources\\ball.jpg")
ball=pygame.transform.scale(ball,(100,100))
ball_rect=ball.get_rect()
clock=pygame.time.Clock()
speed=[5,5]
Running =True
while Running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            Running=False
    clock.tick(60)
    ball_rect=ball_rect.move(speed)
    if ball_rect.left<0 or ball_rect.right>640:
        speed[0]=-speed[0]
    if ball_rect.top<0 or ball_rect.bottom>480:
        speed[1]=-speed[1] 
    screen.fill((0,0,0))
    screen.blit(ball,ball_rect)
    pygame.display.flip()