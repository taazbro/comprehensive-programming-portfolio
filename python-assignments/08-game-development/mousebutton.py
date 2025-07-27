import pygame
import sys

pygame.init()
Screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ball Click Tracker")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

ball_pos = [400, 300]
ball_radius = 20
ball_vel = [3, 3]
Clicks = 0

running = True
while running:
	Screen.fill((255, 0, 0)) 
	pygame.draw.circle(Screen, (0, 0, 255), ball_pos, ball_radius)
text = font .render(f"clicks: {clicks}", true, (255,255,255))
screen.blit(text, (30, 30))
	

for i in range(2):
		Ball_pos[i] += balll_vel[i]
if ball_pos[i] < ball_radius or ball_pos[i] > (800 if i == 0 else 600) - ball_radius:
			Ball_veil[i] *= -1
pip
for event in pygame.event.get():
	if event.type == pygame.QUIT:
			Running = false
	elif event.type == pygame.MOUSEBUTTONDOWN:
			Mx, my = pygame.mouse.get_pos()
	distance = ((mx - ball_pos[0]**2 + (my - ball_pos[1])**2)**0.5)
	if distance <= ball_radius:
				clicks += 1 

	pygame.display.flip()
	clock.tick(60)

	
pygame.quit()
sys.exit() 

