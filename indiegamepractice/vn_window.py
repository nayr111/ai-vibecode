import pygame
import sys

# 1. Initialize Pygame and its font system
pygame.init()

# 2. Setup the Game Window (800 pixels wide, 600 pixels tall)
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Indie Visual Novel Engine")
clock = pygame.time.Clock()

# 3. Colors (Red, Green, Blue values from 0 to 255)
BG_COLOR = (30, 30, 46)        # Deep dark slate background
BOX_COLOR = (255, 225, 235)    # Soft DDLC-style pastel pink dialogue box
BORDER_COLOR = (255, 105, 180) # Hot pink border
TEXT_COLOR = (40, 40, 40)      # Dark gray text

# 4. Fonts
name_font = pygame.font.SysFont("arial", 28, bold=True)
text_font = pygame.font.SysFont("arial", 24)

# 5. Dialogue Data (Just like our list of dictionaries!)
dialogue_lines = [
    {"speaker": "Sayori", "text": "Whoa! We're out of the terminal and inside a real window!"},
    {"speaker": "Monika", "text": "Click anywhere on the screen or press SPACE to continue."},
    {"speaker": "Sayori", "text": "You just built a real 60 FPS game loop in Python!"}
]
current_line_index = 0

# --- THE MAIN 60 FPS GAME LOOP ---
running = True
while running:
    # A. CHECK EVENTS (Keyboard & Mouse)
    for event in pygame.event.get():
        # If the player clicks the window's 'X' button
        if event.type == pygame.QUIT:
            running = False
            
        # Advance dialogue on Mouse Click OR Spacebar press!
        if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            current_line_index += 1
            # Loop back to the start if we reach the end of the list
            if current_line_index >= len(dialogue_lines):
                current_line_index = 0

    # B. DRAW EVERYTHING ONTO THE SCREEN
    # 1. Fill the background
    screen.fill(BG_COLOR)
    
    # 2. Draw the Dialogue Box at the bottom (x, y, width, height)
    box_rect = pygame.Rect(50, 400, 700, 160)
    pygame.draw.rect(screen, BOX_COLOR, box_rect, border_radius=15)
    pygame.draw.rect(screen, BORDER_COLOR, box_rect, width=4, border_radius=15)
    
    # 3. Render the current Speaker and Text onto surfaces
    current_data = dialogue_lines[current_line_index]
    speaker_surface = name_font.render(current_data["speaker"], True, BORDER_COLOR)
    text_surface = text_font.render(current_data["text"], True, TEXT_COLOR)
    
    # 4. Blit (stamp) the text onto the screen at specific X, Y coordinates
    screen.blit(speaker_surface, (80, 415))
    screen.blit(text_surface, (80, 460))

    # C. FLIP THE DISPLAY & CAP AT 60 FPS
    pygame.display.flip()
    clock.tick(60)

# Cleanly exit Python when the loop ends
pygame.quit()
sys.exit()
