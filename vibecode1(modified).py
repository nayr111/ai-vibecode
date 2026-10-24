QUESTIONS = [
    {
        "question": "What Pokemon game's mascot is Rayquaza?",
        "choices": ["Ruby", "Sapphire", "Emerald", "Diamond"],
        "answer": "C",
    },
    {
        "question": "What is the third region that is visited in Genshin Impact?",
        "choices": ["Mondstadt", "Fontaine", "Liyue", "Inazuma"],
        "answer": "D",
    },
    {
        "question": "Which of the following is NOT a programming language?",
        "choices": ["Python", "Snake", "C++", "Java"],
        "answer": "B",
    },
    {
        "question": "Hey, it's me, it's [?]!",
        "choices": ["Verity", "Falsity", "Cruelty", "Lovity"],
        "answer": "A",
    },
    {
        "question": "Which of the following is NOT a Re: Zero character?",
        "choices": ["Rem", "Ram", "Rom", "Rum"],
        "answer": "D",
    },
]
LETTERS = ["A", "B", "C", "D"]
def ask_question(number, q):
    """
    Show a single question and keep asking until the player gets it right.
    Returns True if they got it right on the FIRST try (used for scoring).
    """
    print(f"\nQuestion {number} of {len(QUESTIONS)}")
    print(q["question"])

    for letter, choice in zip(LETTERS, q["choices"]):
        print(f"  {letter}) {choice}")

    first_try = True  
    
    while True:
        
        guess = input("Your answer (A/B/C/D): ").strip().upper()

        if guess not in LETTERS:
            print("Please enter A, B, C, or D.")
        elif guess == q["answer"]:
            print("Correct! 🎉")
            return first_try  
        else:
            print("Wrong answer, try again.")
            first_try = False  

def play_quiz():
    """Run through all the questions once and show the final score."""
    score = 0

    for number, q in enumerate(QUESTIONS, start=1):
        if ask_question(number, q):
            score += 1  

    print(f"\nQuiz complete! You got {score} out of {len(QUESTIONS)} on the first try.")


def main():
    print("=== Welcome to the Quiz Game! ===")

    while True:
        play_quiz()

        while True:
            choice = input("\nPlay again (P) or exit (E)? ").strip().upper()
            if choice in ("P", "E"):
                break  
            print("Please enter P or E.")

        if choice == "E":
            print("Thanks for playing. Goodbye!")
            break 
        


if __name__ == "__main__":
    main()