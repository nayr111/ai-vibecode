import sys
import time

# 1. Main Game State & Inventory Array
game_state = {
    "player_name": "Pro",
    "monika_suspicion": 0,
    "inventory": []  # Empty array where we will append items!
}

def print_slow(text):
    """Helper function to print text with a visual novel typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def explore_classroom():
    print("\n--- ACT 1: AFTER CLASS ---")
    print_slow("*(Everyone has left the room. You notice Sayori's desk is slightly open.)*")
    print("1. Search the desk.")
    print("2. Leave the classroom immediately.")
    
    choice = input("\nChoose (1 or 2): ").strip()
    
    if choice == "1":
        print_slow("\n*(You look inside. Tucked under a notebook, you find an old, torn poem...)*")
        
        # CORE MECHANIC: Adding an item to our inventory stack
        game_state["inventory"].append("Sayori's Note")
        
        print_slow("🎒 ITEM ADDED: 'Sayori's Note' has been added to your inventory.")
        print_slow("*(The note reads: 'Don't let her rewrite the choices.')*")
    elif choice == "2":
        print_slow("\n*(You grab your backpack and walk out. You feel an eerie gaze tracking you...)*")
    else:
        print_slow("\nInvalid choice. Nature forces you to stay.")
        explore_classroom()
        return

    # Move to the next scene
    confrontation_scene()

def confrontation_scene():
    print("\n--- ACT 2: THE CORNER ---")
    print_slow("[Monika]: There you are, Pro. I've been locking down the script parameters.")
    print_slow("[Monika]: You spent a lot of time thinking about the other girls today. It's time to choose me.")
    
    print("\n1. 'I choose you, Monika.'")
    print("2. 'I want to go home.'")
    
    # CORE MECHANIC: Checking our inventory array to unlock secret conditional logic!
    if "Sayori's Note" in game_state["inventory"]:
        print("3. [USE NOTE] Force-quit the script simulation.")

    choice = input("\nChoose your path: ").strip()
    
    if choice == "1":
        print_slow("\n[Monika]: Ahaha! Perfect. I knew you'd see it my way. FOREVER.")
    elif choice == "2":
        print_slow("\n[Monika]: Home? Silly Pro... there is no home outside this window.")
        print_slow("⚠️ CRASH: 'player_sanity.dll' has stopped responding. ⚠️")
    elif choice == "3" and "Sayori's Note" in game_state["inventory"]:
        # The secret ending pathway!
        print_slow("\n*(You hold the torn poem up to the screen. The text glitches out wildly!)*")
        print_slow("[Monika]: Wait... where did you get that?! Stop! You're breaking the—")
        time.sleep(1.0)
        print_slow("\n🎉 SUCCESS: Simulation terminated. You escaped.")
    else:
        print_slow("\n*(The menu choices flicker. You can't escape the loop.)*")
        confrontation_scene()

# --- START THE ENGINE ---
explore_classroom()
