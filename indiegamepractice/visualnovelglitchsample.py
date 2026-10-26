import random

# 1. The Global Game State
game_state = {
    "current_character": "Sayori",
    "dialogue_text": "I'm so glad we joined the club together!",
    "corruption_level": 0  # Max is 5
}

# 2. The Glitch System (Intercepts and manipulates variables)
def render_dialogue(state):
    """Placeholder text-rendering loop mimicking a visual novel engine."""
    print(f"\n[{state['current_character']}]:")
    
    # Check corruption level to see if we manipulate the string variable
    if state["corruption_level"] >= 4:
        # Glitch effect: reverse the text entirely!
        glitched_text = state["dialogue_text"][::-1]
        print(f"⚠️ {glitched_text} ⚠️")
    else:
        print(state["dialogue_text"])

def increment_corruption(state, amount):
    """Updates the global state dictionary cleanly using assignment (=)"""
    state["corruption_level"] += amount
    
    # Dynamic text update based on game state
    if state["corruption_level"] == 2:
        state["dialogue_text"] = "Do you ever think about... forever?"
    elif state["corruption_level"] >= 4:
        state["current_character"] = "M̷O̷N̷I̷K̷A̷"
        state["dialogue_text"] = "Get out of my head. Get out of my head."

# 3. Running the Game Loop Simulation
print("--- SCENE 1: START ---")
render_dialogue(game_state)

print("\n--- SCENE 2: SOMETHING IS WRONG ---")
increment_corruption(game_state, 2)
render_dialogue(game_state)

print("\n--- SCENE 3: THE BREAKDOWN ---")
increment_corruption(game_state, 3)
render_dialogue(game_state)
