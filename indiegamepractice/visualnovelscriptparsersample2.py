import sys
import time

# 1. Clear Game State & Inventory Array
game_state = {
    "player_name": "Pro",
    "inventory": [] # Our item memory stack
}

def print_slow(text):
    """Helper function to print text with a visual novel typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def parse_story_file(filename):
    """Reads our file and returns a raw list of cleaned lines."""
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]

def play_engine(raw_lines):
    print("\n--- INDIE ENGINE: PARSING INVENTORY FLAGS ---")
    
    for line in raw_lines:
        # PATH 1: Handle item pickup lines (🎒GET|Item Name)
        if line.startswith("🎒GET"):
            parts = line.split("|")
            item_name = parts[1]
            game_state["inventory"].append(item_name)
            print(f"\n🎒 [INVENTORY UPDATE]: Added '{item_name}' to your backpack.")
            input("*(Press Enter)*")
            continue
            
        # PATH 2: Handle conditional locked lines (🔒REQ:Item Name|Speaker|Text)
        if line.startswith("🔒REQ"):
            parts = line.split("|") # ['🔒REQ:Silver Key', 'Monika', 'Wait...']
            
            # Extract the item name from the first chunk by removing '🔒REQ:'
            required_item = parts[0].replace("🔒REQ:", "")
            speaker = parts[1]
            text = parts[2]
            
            # DEFENSIVE GUARD CHECK: If they DON'T have the item, skip this text line entirely!
            if required_item not in game_state["inventory"]:
                continue
            
            # If they pass the check, display the secret text branch
            print(f"\n[{speaker}]:")
            print_slow(f"✨ {text}")
            input("*(Press Enter)*")
            continue
            
        # PATH 3: Handle completely normal dialogue lines (Speaker|Text)
        parts = line.split("|")
        speaker = parts[0]
        text = parts[1]
        
        print(f"\n[{speaker}]:")
        print_slow(text)
        input("*(Press Enter)*")

    print("\n--- END OF SIMULATION ---")

# --- EXECUTE THE SYSTEM ---
# 1. Gather lines from our text file
script_data = parse_story_file("story2.txt")

# 2. Run our advanced condition game loop!
play_engine(script_data)
