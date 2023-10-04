import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BALL_SPEED = 5
PADDLE_SPEED = 15

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пинг-Понг")

ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = BALL_SPEED
ball_speed_y = BALL_SPEED

left_paddle_x = 50
left_paddle_y = HEIGHT // 2 - 50
left_paddle_speed = 0

right_paddle_x = WIDTH - 50
right_paddle_y = HEIGHT // 2 - 50
right_paddle_speed = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                left_paddle_speed = -PADDLE_SPEED
            elif event.key == pygame.K_s:
                left_paddle_speed = PADDLE_SPEED
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                left_paddle_speed = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                right_paddle_speed = -PADDLE_SPEED
            elif event.key == pygame.K_DOWN:
                right_paddle_speed = PADDLE_SPEED
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                right_paddle_speed = 0

    left_paddle_y += left_paddle_speed
    right_paddle_y += right_paddle_speed

    left_paddle_y = max(0, min(left_paddle_y, HEIGHT - 100))
    right_paddle_y = max(0, min(right_paddle_y, HEIGHT - 100))

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_y <= 0 or ball_y >= HEIGHT - 20:
        ball_speed_y = -ball_speed_y

    if (
        ball_x <= left_paddle_x + 20
        and left_paddle_y <= ball_y <= left_paddle_y + 100
    ) or (
        ball_x >= right_paddle_x - 20
        and right_paddle_y <= ball_y <= right_paddle_y + 100
    ):
        ball_speed_x = -ball_speed_x

    if ball_x < 0 or ball_x > WIDTH:
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_speed_x = BALL_SPEED
        ball_speed_y = BALL_SPEED

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, WHITE, (left_paddle_x, left_paddle_y, 20, 100))
    pygame.draw.rect(screen, WHITE, (right_paddle_x, right_paddle_y, 20, 100))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, 20, 20))
    pygame.display.flip()
    pygame.time.delay(30)
