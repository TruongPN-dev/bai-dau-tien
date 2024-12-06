import pygame
import numpy as np
import math
import random

class Ball:
    def __init__(self, position, velocity):
        self.pos = np.array(position, dtype=np.float64)
        self.v = np.array(velocity, dtype=np.float64)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.is_in = True

def draw_arc(window, center, radius, start_angle, end_angle):
    p1 = center + (radius + 1000) * np.array([math.cos(start_angle), math.sin(start_angle)])
    p2 = center + (radius + 1000) * np.array([math.cos(end_angle), math.sin(end_angle)])
    pygame.draw.polygon(window, black, [center, p1, p2], 0)

def is_ball_in_arc(ball_pos, circle_center, start_angle, end_angle):
    dx = ball_pos[0] - circle_center[0]
    dy = ball_pos[1] - circle_center[1]
    ball_angle = math.atan2(dy, dx)
    start_angle = start_angle % (2 * math.pi)
    end_angle = end_angle % (2 * math.pi)
    if start_angle > end_angle:
        end_angle += 2 * math.pi
    if start_angle <= ball_angle <= end_angle or (start_angle <= ball_angle + 2 * math.pi <= end_angle):
        return True
pygame.init()
width, height = 800, 800
window = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
orange = (255,165,0)
red = (255,0,0)
black = (0,0,0)
circle_center = np.array([width/2, height/2], dtype=np.float64)
circle_radius = 250
ball_radius = 5
ball_pos = np.array([width/2, height/2-240], dtype=np.float64)
running = True
gravity = 0.2
ball_vel = np.array([0,0], dtype=np.float64)
arc_degrees = 60
start_angle = math.radians(-arc_degrees / 2)
end_angle = math.radians(arc_degrees / 2)
spinning_speed = 0.01
balls = [Ball(ball_pos, ball_vel)]
f = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    start_angle += spinning_speed
    end_angle += spinning_speed
    for ball in balls:
        if ball.pos[1] > height or ball.pos[0] < 0 or ball.pos[0] > width or ball.pos[1] < 0:
            balls.remove(ball)
            f -= 1
            balls.append(Ball(position=[width // 2, height // 2 - 240], velocity=[random.uniform(-4,4),random.uniform(-1,1)]))
            balls.append(Ball(position=[width // 2, height // 2 - 240], velocity=[random.uniform(-4,4),random.uniform(-1,1)]))
            f += 2
            print(f'\r{f}', end='', flush=True)
        ball.v[1] += gravity
        ball.pos+= ball.v
        dist = np.linalg.norm(ball.pos - circle_center)
        if dist + ball_radius > circle_radius:
            if is_ball_in_arc(ball.pos, circle_center, start_angle, end_angle):
                ball.is_in = False
            if  ball.is_in:
                d = ball.pos - circle_center
                d_unit = d/np.linalg.norm(d)
                ball.pos = circle_center + (circle_radius - ball_radius) * d_unit
                t = np.array([-d[1],d[0]], dtype=np.float64)
                proj_v_t = (np.dot(ball.v,t)/np.dot(t,t)) * t
                ball.v = 2 * proj_v_t - ball.v
                ball.v += t * spinning_speed
    window.fill(black)
    pygame.draw.circle(window, orange, circle_center, circle_radius, 3)
    draw_arc(window, circle_center, circle_radius, start_angle, end_angle)
    for ball in balls:
        pygame.draw.circle(window, ball.color, ball.pos, ball_radius)
    pygame.display.flip()
    clock.tick(60)
pygame.quit
