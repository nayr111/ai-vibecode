import sys
import time
import random

def print_slow(text):
    """Helper function to print text with a visual novel typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def parse_story_file(filename):
    """
    Reads a plain text file, cuts each line at the '|' character,
    and returns a beautifully structured list of dictionaries.
    """
    structured_script = []
    
    # Python's built-in file reader wrapper
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            cleaned_line = line.strip() # Remove invisible newline breaks (\n)
            
            # Guard Clause: Skip completely empty lines in our text file
            if not cleaned_line:
                continue
                
            # THE MAGIC SPLIT: Slices the line at the '|' into two clean parts
            # "Sayori|Hey!" becomes parts[0] = "Sayori", parts[1] = "Hey!"
            parts = cleaned_line.split("|")
            
            # Pack it safely into our dictionary layout
            dialogue_dict = {
                "speaker": parts[0],
                "text": parts[1]
            }
            
            # Append it into our main narrative stack
            structured_script.append(dialogue_dict)
            
    return structured_script

def play_game(script):
    print("\n--- THE LITERATURE CLUB: LOADING FROM TEXT FILE ---")
    
    for line in script:
        speaker = line["speaker"]
        text = line["text"]
        
        # SCRIPT INTERCEPTOR: The engine scans the data before rendering it
        if speaker == "Sayori":
            # 30% chance to corrupt Sayori's dialogue as Act 1 breaks down
            if random.random() < 0.30:
                speaker = "S̶A̶Y̶O̶R̶I̶"
                # Keep only every second letter and capitalize it to create a creepy glitch text
                text = "I CAN'T GET OUT OF MY HEAD. " + text.upper()[::2]
        
        print(f"\n[{speaker}]:")
        print_slow(text)
        
        input("*(Press Enter)*")
        
    print("\n--- END OF TEXT SCRIPT ---")

# --- EXECUTE THE ENGINE ---
# 1. Parse the text file and transform it into code data
loaded_story = parse_story_file("story.txt")

# 2. Feed that freshly parsed list into our game loop!
play_game(loaded_story)
