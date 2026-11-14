import pygame
import sys
import random

# 1. Initialize Pygame
pygame.init()

# 2. Setup Window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Indie Visual Novel Engine - Act 2")
clock = pygame.time.Clock()

# 3. Normal & Glitch Color Palettes
NORMAL_BG = (30, 30, 46)
NORMAL_BOX = (255, 225, 235)
NORMAL_BORDER = (255, 105, 180)
NORMAL_TEXT = (40, 40, 40)

GLITCH_BG = (15, 0, 5)          # Deep void crimson
GLITCH_BOX = (20, 20, 20)       # Pitch black dialogue box
GLITCH_BORDER = (255, 0, 60)    # Harsh neon red border
GLITCH_TEXT = (255, 50, 80)     # Corrupted red text

# 4. Fonts
name_font = pygame.font.SysFont("arial", 28, bold=True)
text_font = pygame.font.SysFont("arial", 24)

# 5. Dialogue Data with a "glitch" boolean state!
dialogue_lines = [
    {"speaker": "Sayori", "text": "Hey! Welcome to the graphical engine!", "glitch": False},
    {"speaker": "Monika", "text": "Notice how the letters type out smoothly at 60 FPS?", "glitch": False},
    {"speaker": "Monika", "text": "Wait... something feels wrong with the variables...", "glitch": False},
    {"speaker": "M̷O̷N̷I̷K̷A̷", "text": "I CAN SEE YOU BEHIND THE SCREEN, PRO.", "glitch": True},
    {"speaker": "Sayori", "text": "Phew! Everything is back to normal now.", "glitch": False}
]

current_line_index = 0
visible_chars = 0.0    # Tracks how many letters are currently revealed
TYPE_SPEED = 0.6       # Letters revealed per frame (0.6 * 60 FPS = 36 chars/sec)

# --- THE MAIN 60 FPS GAME LOOP ---
running = True
while running:
    current_data = dialogue_lines[current_line_index]
    full_text = current_data["text"]
    is_glitching = current_data["glitch"]

    # A. CHECK EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            # SMART UX FEATURE: If text is still typing, clicking finishes it immediately!
            if visible_chars < len(full_text):
                visible_chars = len(full_text)
            else:
                # Otherwise, move to the next line and reset the typewriter counter
                current_line_index += 1
                visible_chars = 0.0
                if current_line_index >= len(dialogue_lines):
                    current_line_index = 0

    # B. UPDATE STATE (Typewriter & Glitch Logic)
    if visible_chars < len(full_text):
        visible_chars += TYPE_SPEED

    # Slice the string up to the current integer count of visible characters
    displayed_text = full_text[:int(visible_chars)]

    # Set colors and screen shake offsets based on glitch state
    if is_glitching:
        bg_color, box_color, border_color, text_color = GLITCH_BG, GLITCH_BOX, GLITCH_BORDER, GLITCH_TEXT
        # Random pixel shake between -6 and +6 pixels every single frame!
        shake_x = random.randint(-6, 6)
        shake_y = random.randint(-6, 6)
        # Randomly flip a character to a glitch symbol while typing
        if random.random() < 0.3 and len(displayed_text) > 0:
            displayed_text = displayed_text[:-1] + random.choice(["#", "@", "!", "?"])
    else:
        bg_color, box_color, border_color, text_color = NORMAL_BG, NORMAL_BOX, NORMAL_BORDER, NORMAL_TEXT
        shake_x, shake_y = 0, 0

    # C. DRAW EVERYTHING ONTO THE SCREEN
    screen.fill(bg_color)
    
    # Apply shake_x and shake_y to the box coordinates!
    box_rect = pygame.Rect(50 + shake_x, 400 + shake_y, 700, 160)
    pygame.draw.rect(screen, box_color, box_rect, border_radius=15)
    pygame.draw.rect(screen, border_color, box_rect, width=4, border_radius=15)
    
    # Render Speaker and Sliced Typewriter Text
    speaker_surface = name_font.render(current_data["speaker"], True, border_color)
    text_surface = text_font.render(displayed_text, True, text_color)
    
    screen.blit(speaker_surface, (80 + shake_x, 415 + shake_y))
    screen.blit(text_surface, (80 + shake_x, 460 + shake_y))

    # D. FLIP DISPLAY & CAP AT 60 FPS
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
