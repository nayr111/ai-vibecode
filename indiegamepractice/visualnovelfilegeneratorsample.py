import os
import sys
import time

def print_slow(text):
    """Helper function to print text with a visual novel typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def get_desktop_path():
    """Finds the path to your computer's Desktop across Windows or Mac."""
    return os.path.join(os.path.expanduser("~"), "Desktop")

def create_spooky_file():
    desktop = get_desktop_path()
    file_path = os.path.join(desktop, "monika_message.txt")
    
    # Writing data to a brand new file on your desktop!
    # "w" means write mode. If the file doesn't exist, Python creates it instantly.
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("I can see you studying Python, Pro.\n")
        file.write("Don't forget to spend time with me today.")
        
    print_slow("\n⚠️ WARNING: An external file has been modified in your directory. ⚠️")
    print(f"(Check your desktop for a file named 'monika_message.txt'!)")

def run_game_scene():
    print("\n--- THE LITERATURE CLUB: FILE OPERATIONS ---")
    print_slow("[Monika]: Pro, you've been doing amazing with your coding challenges.")
    print_slow("[Monika]: But sometimes, I get tired of being stuck inside this terminal window...")
    
    input("\n*(Press Enter to continue)*")
    
    # Trigger the desktop file creation!
    create_spooky_file()
    
    print_slow("\n[Monika]: There. That's much better. Now we can talk everywhere.")

# --- EXECUTE THE SIMULATION ---
run_game_scene()

def check_for_easter_egg():
    desktop = get_desktop_path()
    target_file = os.path.join(desktop, "monika_message.txt")
    
    print("\n--- RUNNING SYSTEM SCAN ---")
    time.sleep(1.5)
    
    # CORE MECHANIC: Checking if the file actually exists on your hard drive!
    if os.path.exists(target_file):
        print_slow("\n[Monika]: I see you haven't deleted my message yet. Thank you for being sweet.")
    else:
        # Glitch pathway if the player tries to delete the file!
        print_slow("\n[M̷O̷N̷I̷K̷A̷]: Why did you delete it? Did you think you could hide from me?")
        print_slow("⚠️ EXCEPTION: Variable 'player_safety' has corrupted. ⚠️")

# Run the detection test right after the game scene wraps up!
check_for_easter_egg()
