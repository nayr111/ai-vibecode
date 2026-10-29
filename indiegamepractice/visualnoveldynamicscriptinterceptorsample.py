import random # Make sure this is imported at the very top of your file!

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
