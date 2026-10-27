import sys
import time

# 1. Main Game State
game_state = {
    "player_name": "Pro",
    "monika_suspicion": 0,
    "current_act": 1
}

def print_slow(text):
    """Helper function to print text with a visual novel typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def start_scene():
    print("\n--- THE LITERATURE CLUB: ACT 1 ---")
    print_slow("[Monika]: Welcome back to the club room! I was hoping you'd walk in next.")
    print_slow("[Monika]: I've been organizing our weekly poem swap. Would you like to read mine first?")
    
    print("\n1. 'I'd love to read your poem, Monika!'")
    print("2. 'Actually, I wanted to show my poem to Sayori first.'")
    
    # Catching player input
    choice = input("\nChoose (1 or 2): ").strip()
    
    # Branching Logic
    if choice == "1":
        game_state["monika_suspicion"] += 0
        print_slow("\n[Monika]: Ah, you make me so happy! Here, tell me what you think...")
        print_slow("*(You read her poem. It's written in perfectly clean handwriting.)*")
        
    elif choice == "2":
        # Spiking suspicion changes the state of the game!
        game_state["monika_suspicion"] += 3
        print_slow("\n[Monika]: Oh... Sayori?")
        time.sleep(1.0) # Eerie pause
        print_slow("[Monika]: ...I see. Don't worry, she'll be around later. For a long, long time.")
        
    else:
        # Guard clause for invalid inputs!
        print_slow("\n*(You hesitate, trying to look away from the screen...)*")
        print_slow("[Monika]: Pro... you have to choose.")
        # Re-run the scene if they typed something weird
        start_scene()
        return

    # Triggering the consequences of the player's choice
    check_game_corruption()

def check_game_corruption():
    print("\n--- NEXT DAY ---")
    
    # The game reacts dynamically to the suspicion variable
    if game_state["monika_suspicion"] >= 3:
        # Glitch pathway
        game_state["current_act"] = 2
        glitched_title = "[M̷O̷N̷I̷K̷A̷]"
        print(f"\n{glitched_title}:")
        print_slow("Why would you choose her over me? It's just a game, right?")
        print_slow("⚠️ EXCEPTION: Script 'sayori.chr' has been broken or deleted. ⚠️")
    else:
        # Normal pathway
        print_slow("\n[Sayori]: Good morning! Did you bring a snack today?")
        print_slow("*(The club feels peaceful and bright.)*")

# Start the game simulation!
start_scene()
