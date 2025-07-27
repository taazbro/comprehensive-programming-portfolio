# Assignment 9 
# Name: Tanjim Ahmed Al Zabeer

import pygame
import sys
import random
import time

pygame.init()

# Now we gonna Setup the screen.
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Timed Color Catch Ball Game")
clock = pygame.time.Clock()

# Here we gonna set the Font
font = pygame.font.SysFont("Arial", 22)

# Let's start the Ball Setup
ball_pos = [300, 200]
ball_vel = [3.6, 3.6]  # 10% slower speed
ball_radius = 20

# I need Score and hit counters to know player ability
score = 0
red_hits = 0
green_hits = 0
blue_hits = 0
yellow_hits = 0

# Now we predefine the color sequence: red, green, blue, yellow ( tell me your favorite color)
color_sequence = [
    (255, 0, 0),     # Red
    (0, 200, 0),     # Green
    (0, 0, 255),     # Blue
    (255, 255, 0),   # Yellow
    (255, 0, 0),
    (0, 200, 0),
    (0, 0, 255),
    (255, 255, 0)
]
color_index = 0
start_time = time.time()
current_bg = color_sequence[color_index]

# Game duration: 2 minutes
game_start = time.time()

# Here we will create the Function to draw text
def draw_text(text, y, color=(0, 0, 0)):
    label = font.render(text, True, color)
    rect = label.get_rect(center=(WIDTH // 2, y))
    screen.blit(label, rect)

# Here i am setting up the Game Loop
running = True
while running:
    screen.fill(current_bg)

    # Now we will Display score info
    draw_text(f"Score: {score}", 30)
    draw_text(f"Red Hits: {red_hits} | Green Hits: {green_hits} | Blue Hits: {blue_hits} | Yellow Hits: {yellow_hits}", 60)
    draw_text(f"Time Remaining: {int(120 - (time.time() - game_start))}s", 90)

    # In here i will make it Draw and move the ball
    pygame.draw.circle(screen, (100, 100, 255), ball_pos, ball_radius)
    for i in range(2):
        ball_pos[i] += ball_vel[i]
        if ball_pos[i] < ball_radius or ball_pos[i] > (WIDTH if i == 0 else HEIGHT) - ball_radius:
            ball_vel[i] *= -1

    # Here I will Check for color transition 
    elapsed = time.time() - start_time
    if elapsed >= 5:
        color_index += 1
        if color_index >= len(color_sequence):
            running = False  # End game after all colors cycled
        else:
            current_bg = color_sequence[color_index]
            start_time = time.time()

    # I am cool at Event handling, huh;
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            distance = ((mx - ball_pos[0]) ** 2 + (my - ball_pos[1]) ** 2) ** 0.5
            if distance <= ball_radius:
                score += 1
                if current_bg == (255, 0, 0):
                    red_hits += 1
                elif current_bg == (0, 200, 0):
                    green_hits += 1
                elif current_bg == (0, 0, 255):
                    blue_hits += 1
                elif current_bg == (255, 255, 0):
                    yellow_hits += 1

    if time.time() - game_start >= 120:
        running = False

    pygame.display.flip()
    clock.tick(60)

# This is where i show the Final screen and take my leave
screen.fill((255, 255, 255))
draw_text("Time's up!", 120)
draw_text(f"Final Score: {score}", 160)
draw_text(f"Red Hits: {red_hits} | Green Hits: {green_hits} | Blue Hits: {blue_hits} | Yellow Hits: {yellow_hits}", 200)
pygame.display.flip()
pygame.time.wait(5000)

pygame.quit()
sys.exit()