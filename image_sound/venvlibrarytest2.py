import pygame
from PIL import Image, ImageDraw

# 1. Initialize Pygame
pygame.init()
screen_width, screen_height = 400, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Isolated Safe Sandbox")

# 2. Use PILLOW to create a graphic dynamically in memory
# We create a transparent 50x50 image and draw a bright red block on it
pil_image = Image.new("RGBA", (50, 50), (0, 0, 0, 0))
drawer = ImageDraw.Draw(pil_image)
drawer.rectangle([0, 0, 49, 49], fill=(255, 80, 80)) # Red block

# Convert the Pillow Image into a format Pygame understands
mode = pil_image.mode
size = pil_image.size
data = pil_image.tobytes()
player_sprite = pygame.image.fromstring(data, size, mode)

# Starting position of our player square
player_x = 175
player_y = 175
player_speed = 5

# 3. Game Loop
clock = pygame.time.Clock()
running = True

while running:
    # Look for exit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Check for Key Presses (Arrow Keys)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - 50:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < screen_height - 50:
        player_y += player_speed

    # Drawing everything on screen
    screen.fill((40, 180, 130))               # Draw calm green background
    screen.blit(player_sprite, (player_x, player_y)) # Draw the red Pillow square
    
    pygame.display.flip()
    clock.tick(60) # Lock the game loop to a smooth 60 frames per second

pygame.quit()
