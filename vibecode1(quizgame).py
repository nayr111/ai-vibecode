"""
A simple 5-question multiple-choice quiz game.

How to run:  python quiz_game.py
"""

# ---------------------------------------------------------------
# 1. THE QUESTIONS
# ---------------------------------------------------------------
# Each question is a dictionary with three parts:
#   "question" -> the text we show the player
#   "choices"  -> a list of 4 answer options (index 0 = A, 1 = B, ...)
#   "answer"   -> the letter of the correct choice
# Keeping the data in a list like this means you can add, remove, or
# change questions without touching any of the game logic below.
QUESTIONS = [
    {
        "question": "Who wrote the novel 'Pride and Prejudice'?",
        "choices": ["Charlotte Brontë", "Jane Austen", "Mary Shelley", "George Eliot"],
        "answer": "B",
    },
    {
        "question": "What is the chemical symbol for gold?",
        "choices": ["Ag", "Gd", "Au", "Go"],
        "answer": "C",
    },
    {
        "question": "What is 12 multiplied by 12?",
        "choices": ["124", "144", "132", "148"],
        "answer": "B",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["Mars", "Venus", "Jupiter", "Mercury"],
        "answer": "A",
    },
    {
        "question": "In which Shakespeare play does the character Hamlet appear?",
        "choices": ["Macbeth", "Othello", "King Lear", "Hamlet"],
        "answer": "D",
    },
]

# The valid letters a player is allowed to type.
LETTERS = ["A", "B", "C", "D"]


# ---------------------------------------------------------------
# 2. HELPER FUNCTION: ASK ONE QUESTION
# ---------------------------------------------------------------
def ask_question(number, q):
    """
    Show a single question and keep asking until the player gets it right.
    Returns True if they got it right on the FIRST try (used for scoring).
    """
    print(f"\nQuestion {number} of {len(QUESTIONS)}")
    print(q["question"])

    # zip() pairs each letter with its choice: ("A", "Charlotte Brontë"), ...
    for letter, choice in zip(LETTERS, q["choices"]):
        print(f"  {letter}) {choice}")

    first_try = True  # Tracks whether the player has missed yet

    # Loop until the correct answer is entered
    while True:
        # .strip() removes stray spaces; .upper() lets "b" count as "B"
        guess = input("Your answer (A/B/C/D): ").strip().upper()

        if guess not in LETTERS:
            # Input wasn't A-D, so don't count it as a wrong answer
            print("Please enter A, B, C, or D.")
        elif guess == q["answer"]:
            print("Correct! 🎉")
            return first_try  # Leave the loop and move to the next question
        else:
            print("Wrong answer, try again.")
            first_try = False  # They missed once, so no point for this question


# ---------------------------------------------------------------
# 3. HELPER FUNCTION: PLAY ONE FULL ROUND
# ---------------------------------------------------------------
def play_quiz():
    """Run through all the questions once and show the final score."""
    score = 0

    # enumerate(..., start=1) gives us a question number starting at 1
    for number, q in enumerate(QUESTIONS, start=1):
        if ask_question(number, q):
            score += 1  # Only awarded for first-try correct answers

    print(f"\nQuiz complete! You got {score} out of {len(QUESTIONS)} on the first try.")


# ---------------------------------------------------------------
# 4. MAIN GAME LOOP
# ---------------------------------------------------------------
def main():
    print("=== Welcome to the Quiz Game! ===")

    while True:
        play_quiz()

        # After each round, ask whether to play again or quit
        while True:
            choice = input("\nPlay again (P) or exit (E)? ").strip().upper()
            if choice in ("P", "E"):
                break  # Valid input, leave this small loop
            print("Please enter P or E.")

        if choice == "E":
            print("Thanks for playing. Goodbye!")
            break  # Exit the main loop, which ends the program
        # If choice == "P", the outer loop simply repeats and starts a new round


# This line makes sure main() only runs when you run this file directly
# (and not if another file imports it).
if __name__ == "__main__":
    main()