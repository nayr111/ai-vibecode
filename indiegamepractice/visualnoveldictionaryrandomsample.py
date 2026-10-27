import sys
import time
import random  # Importing Python's random number library!

# 1. Main Game State
game_state = {
    "player_name": "Pro",
    "monika_suspicion": 0
}

# 2. The Dialogue Script (A list of dictionaries)
# Every dictionary represents a single "beat" of the conversation.
act_1_dialogue = [
    {"speaker": "Sayori", "text": "Hey! Thanks for waiting for me after class."},
    {"speaker": "Sayori", "text": "I was thinking we could go grab a snack before the club starts..."},
    {"speaker": "Monika", "text": "Oh, hello you two! I didn't expect to see you together."},
    {"speaker": "Monika", "text": "Are you ready to share your poems today?"}
]

def print_slow(text):
    """Helper function to print text with a visual novel typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def play_dialogue_stream(script_list):
    """Loops through our dialogue data structure and handles random glitch logic."""
    print("\n--- WALKING TO THE CLUB ROOM ---")
    
    for line in script_list:
        speaker = line["speaker"]
        text = line["text"]
        
        # FEATURE 1: RANDOMIZED GLITCH (25% chance of happening per line)
        # random.random() picks a decimal between 0.0 and 1.0. 
        # If it is less than 0.25, the text glitches!
        if random.random() < 0.25:
            # Glitching out the speaker name and reversing the text string
            speaker = "M̷O̷N̷I̷K̷A̷"
            text = text[::-1]
            print(f"\n[{speaker}]:")
            print_slow(f"⚠️ {text} ⚠️")
            game_state["monika_suspicion"] += 1
        else:
            # Normal text rendering
            print(f"\n[{speaker}]:")
            print_slow(text)
            
        # Wait for the player to press enter to proceed to the next line
        input("*(Press Enter)*")

def present_choice():
    print("\n--- THE DECISION ---")
    print_slow("[Monika]: So, Pro... who are you going to show your poem to first?")
    print("1. Sayori")
    print("2. Monika")
    
    choice = input("\nChoose (1 or 2): ").strip()
    
    if choice == "1":
        print_slow("\n[Sayori]: Yay! I can't wait!")
        # If suspicion spiked from random glitches, Monika intercepts!
        if game_state["monika_suspicion"] >= 2:
            time.sleep(1.0)
            print_slow("\n[Monika]: No. You don't want to do that.")
    elif choice == "2":
        print_slow("\n[Monika]: Perfect. I knew you'd make the right choice.")
    else:
        print_slow("\n*(The game window flickers as you hesitate...)*")
        present_choice()

# --- START THE ENGINE ---
# Pass our list of dictionaries straight into our game loop!
play_dialogue_stream(act_1_dialogue)
present_choice()
