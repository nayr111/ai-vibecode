import pygame
import sys
import random
import os

# 1. Initialize Pygame
pygame.init()

# 2. Setup Window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Indie Visual Novel Engine - Full GUI Parser")
clock = pygame.time.Clock()

# 3. Color Palettes
NORMAL_BG = (30, 30, 46)
NORMAL_BOX = (255, 225, 235)
NORMAL_BORDER = (255, 105, 180)
NORMAL_TEXT = (40, 40, 40)

GLITCH_BG = (15, 0, 5)
GLITCH_BOX = (20, 20, 20)
GLITCH_BORDER = (255, 0, 60)
GLITCH_TEXT = (255, 50, 80)

BTN_COLOR = (255, 240, 245)
BTN_HOVER = (255, 180, 210)

# 4. Fonts
name_font = pygame.font.SysFont("arial", 28, bold=True)
text_font = pygame.font.SysFont("arial", 24)

# 5. File Parser (Uses os.path.dirname to always look in the script's own folder!)
def load_script(filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, filename)
    
    parsed_events = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            clean = line.strip()
            if not clean:
                continue
            parts = clean.split("|")
            if parts[0] == "CHOICE":
                parsed_events.append({
                    "type": "CHOICE",
                    "question": parts[1],
                    "opt1": parts[2],
                    "opt2": parts[3]
                })
            else:
                parsed_events.append({
                    "type": parts[0], # "NORMAL" or "GLITCH"
                    "speaker": parts[1],
                    "text": parts[2]
                })
    return parsed_events

# Load our external text file!
script_events = load_script("gui_story.txt")
current_index = 0
visible_chars = 0.0
TYPE_SPEED = 0.6

# Define Button Rectangles (x, y, width, height)
btn1_rect = pygame.Rect(200, 180, 400, 55)
btn2_rect = pygame.Rect(200, 260, 400, 55)

# --- MAIN 60 FPS GAME LOOP ---
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    current_event = script_events[current_index]
    is_choice = (current_event["type"] == "CHOICE")

    # Determine the text to type out
    full_text = current_event["question"] if is_choice else current_event["text"]

    # A. CHECK EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if is_choice:
                # Check if the player clicked inside Button 1 or Button 2!
                if btn1_rect.collidepoint(mouse_pos) or btn2_rect.collidepoint(mouse_pos):
                    current_index = (current_index + 1) % len(script_events)
                    visible_chars = 0.0
            else:
                # Standard dialogue click-to-skip or advance
                if visible_chars < len(full_text):
                    visible_chars = len(full_text)
                else:
                    current_index = (current_index + 1) % len(script_events)
                    visible_chars = 0.0

    # B. UPDATE STATE
    if visible_chars < len(full_text):
        visible_chars += TYPE_SPEED
    displayed_text = full_text[:int(visible_chars)]

    is_glitching = (current_event["type"] == "GLITCH")
    if is_glitching:
        bg_color, box_color, border_color, text_color = GLITCH_BG, GLITCH_BOX, GLITCH_BORDER, GLITCH_TEXT
        shake_x, shake_y = random.randint(-6, 6), random.randint(-6, 6)
        if random.random() < 0.3 and len(displayed_text) > 0:
            displayed_text = displayed_text[:-1] + random.choice(["#", "@", "!", "?"])
    else:
        bg_color, box_color, border_color, text_color = NORMAL_BG, NORMAL_BOX, NORMAL_BORDER, NORMAL_TEXT
        shake_x, shake_y = 0, 0

    # C. DRAW EVERYTHING
    screen.fill(bg_color)

    # Draw Clickable Choice Buttons if we are on a CHOICE line
    if is_choice:
        for rect, label in [(btn1_rect, current_event["opt1"]), (btn2_rect, current_event["opt2"])]:
            # Highlight button when hovering with the mouse!
            color = BTN_HOVER if rect.collidepoint(mouse_pos) else BTN_COLOR
            pygame.draw.rect(screen, color, rect, border_radius=12)
            pygame.draw.rect(screen, NORMAL_BORDER, rect, width=3, border_radius=12)
            
            btn_text = text_font.render(label, True, NORMAL_TEXT)
            text_rect = btn_text.get_rect(center=rect.center)
            screen.blit(btn_text, text_rect)

    # Draw Dialogue Box
    box_rect = pygame.Rect(50 + shake_x, 400 + shake_y, 700, 160)
    pygame.draw.rect(screen, box_color, box_rect, border_radius=15)
    pygame.draw.rect(screen, border_color, box_rect, width=4, border_radius=15)

    speaker_label = "CHOICE" if is_choice else current_event["speaker"]
    speaker_surface = name_font.render(speaker_label, True, border_color)
    text_surface = text_font.render(displayed_text, True, text_color)

    screen.blit(speaker_surface, (80 + shake_x, 415 + shake_y))
    screen.blit(text_surface, (80 + shake_x, 460 + shake_y))

    # D. FLIP & TICK
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
