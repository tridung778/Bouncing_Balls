import pygame
import numpy

pygame.init()
WIDTH, HEIGHT = 800, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
CIRCLE_RADIUS = 150
CIRCLE_CENTER = numpy.array([WIDTH / 2, HEIGHT / 2], dtype=numpy.float64)
BALL_RADIUS = 5
ball_pos = numpy.array([WIDTH / 2, HEIGHT / 2 - 120], dtype=numpy.float64)
GRAVITY = 0.2
ball_vel = numpy.array([0, 0], dtype=numpy.float64)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ball_vel[1] += GRAVITY
    ball_pos += ball_vel
    dist = numpy.linalg.norm(ball_pos - CIRCLE_CENTER)
    if dist + BALL_RADIUS > CIRCLE_RADIUS:
        d = ball_pos - CIRCLE_CENTER
        d_unit = d / numpy.linalg.norm(d)
        ball_pos = CIRCLE_CENTER + (CIRCLE_RADIUS - BALL_RADIUS) * d_unit
        t = numpy.array([-d[1], d[0]], dtype=numpy.float64)
        proj_v_t = (numpy.dot(ball_vel, t) / numpy.dot(t, t)) * t
        ball_vel = 2 * proj_v_t - ball_vel
    window.fill(BLACK)
    pygame.draw.circle(window, ORANGE, CIRCLE_CENTER, CIRCLE_RADIUS, 3)
    pygame.draw.circle(window, RED, ball_pos, BALL_RADIUS, 0)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
