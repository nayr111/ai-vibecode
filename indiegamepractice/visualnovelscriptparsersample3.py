import sys
import time

# 1. Main Game State Tracking
game_state = {
    "player_name": "Pro",
    "points": {
        "Sayori_Points": 0,
        "Natsuki_Points": 0
    },
    "inventory": []
}

# 2. Poem Keyword Database
poem_keywords = {
    "sunny": "Sayori_Points",
    "happy": "Sayori_Points",
    "cupcake": "Natsuki_Points",
    "parfait": "Natsuki_Points"
}

def print_slow(text):
    """Helper function to print text with a visual novel typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def parse_story_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]

def run_poem_minigame():
    print("\n--- 📝 POEM MINIGAME 📝 ---")
    print("Choose 3 words that best describe your poem's mood:")
    words_pool = list(poem_keywords.keys())
    
    for i in range(3):
        print(f"\nRound {i+1}:")
        for idx, word in enumerate(words_pool, 1):
            print(f"{idx}. {word}")
            
        choice = input("Pick a word (1-4): ").strip()
        if choice in ["1", "2", "3", "4"]:
            selected_word = words_pool[int(choice) - 1]
            target_stat = poem_keywords[selected_word]
            game_state["points"][target_stat] += 1
            print(f"✨ Points added to {target_stat.replace('_Points', '')}!")
        else:
            print("Invalid word chosen. You scribbled nonsense.")

def handle_item_choice(parts):
    # Format: 🤔CHOICE|RequiredItem|Option1Text|Option2Text
    required_item = parts[1]
    opt1 = parts[2]
    opt2 = parts[3]
    
    if required_item in game_state["inventory"]:
        print(f"\n🤔 [CHOICE TRIGGERED] You are holding: {required_item}")
        print(f"1. {opt1}")
        print(f"2. {opt2}")
        
        user_choice = input("\nWhat will you do? (1 or 2): ").strip()
        if user_choice == "1":
            print_slow(f"\n*(You step forward and select: {opt1})*")
            print_slow("[Monika]: Oh... is that for me? Thank you, Pro. I'll keep this forever.")
            game_state["inventory"].remove(required_item)
        else:
            print_slow(f"\n*(You step back and select: {opt2})*")
            print_slow("[Monika]: Hmph. Fine. Keep your little secrets to yourself.")
    else:
        print_slow("\n*(You walk past Monika quietly. You don't have any items to interact with.)*")

def play_engine(raw_lines):
    print("\n--- INDIE ENGINE: RUNNING ADVANCED CORE ---")
    
    for line in raw_lines:
        parts = line.split("|")
        flag = parts[0]
        
        # Token Path 1: Trigger Poem Minigame
        if flag == "📝POEM":
            run_poem_minigame()
            continue
            
        # Token Path 2: Trigger Item Interaction Choice
        if flag == "🤔CHOICE":
            handle_item_choice(parts)
            continue
            
        # Token Path 3: Handle Automatic Item Pickups
        if flag == "🎒GET":
            item_name = parts[1]
            game_state["inventory"].append(item_name)
            print(f"\n🎒 [INVENTORY]: Added '{item_name}' to your backpack.")
            input("*(Press Enter)*")
            continue
            
        # Token Path 4: Handle Condition-Locked Lines (Points & Items)
        if flag.startswith("🔒REQ:"):
            condition_expr = flag.replace("🔒REQ:", "") # "Sayori_Points>=2"
            
            # Parsing out mathematical logic from text tokens
            if ">=" in condition_expr:
                stat_name, threshold_str = condition_expr.split(">=")
                threshold = int(threshold_str)
                
                # Check point value out of our nested points state directory
                if game_state["points"].get(stat_name, 0) < threshold:
                    continue # Skip the line if points are too low!
            
            # Handle lines nested beneath point check paths
            speaker = parts[1]
            text = parts[2]
            
            # Nested item check if the conditional text triggers another action flag
            if speaker == "🎒GET":
                game_state["inventory"].append(text)
                print(f"\n🎒 [INVENTORY UNLOCKED]: Added '{text}' to your backpack.")
                input("*(Press Enter)*")
                continue
                
            print(f"\n[{speaker}]:")
            print_slow(text)
            input("*(Press Enter)*")
            continue
            
        # Token Path 5: Completely Normal Text
        speaker = parts[0]
        text = parts[1]
        print(f"\n[{speaker}]:")
        print_slow(text)
        input("*(Press Enter)*")

    print("\n--- GAME LOOP COMPLETE ---")

# --- KICKSTART SYSTEM ---
script_data = parse_story_file("story3.txt")
play_engine(script_data)
