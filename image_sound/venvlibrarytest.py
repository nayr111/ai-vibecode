import pygame
from PIL import Image

print(f"Pillow version: {Image.__version__} is securely loaded!")

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("My Isolated Safe Sandbox")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((40, 180, 130)) # A calm green background
    pygame.display.flip()

pygame.quit()
