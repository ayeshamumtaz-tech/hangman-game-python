import random

# -----------------------------
# Hangman Game
# -----------------------------

hangman_stages = [
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',

'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',

'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',

'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',

'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',

'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',

'''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

easy_words = [
    "book", "apple", "chair", "phone", "table",
    "mouse", "water", "school", "friend", "house"
]

medium_words = [
    "python", "science", "student", "computer",
    "internet", "keyboard", "program", "library"
]

hard_words = [
    "artificial", "intelligence", "programming",
    "developer", "algorithm", "cybersecurity",
    "engineering", "technology"
]

while True:

    print("\n====================================")
    print("      WELCOME TO HANGMAN GAME")
    print("====================================")

    print("\nSelect Difficulty")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    choice = input("Enter choice (1-3): ")

    if choice == "1":
        word = random.choice(easy_words)
    elif choice == "2":
        word = random.choice(medium_words)
    elif choice == "3":
        word = random.choice(hard_words)
    else:
        print("Invalid Choice! Easy level selected.")
        word = random.choice(easy_words)

    guessed_letters = []
    attempts = 6
    score = 0

    while attempts > 0:

        print(hangman_stages[attempts])

        display = ""

        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        print("Word :", display)
        print("Guessed Letters :", " ".join(guessed_letters))
        print("Remaining Attempts :", attempts)
        print("Score :", score)

        if "_" not in display:
            print("\n🎉 Congratulations!")
            print("You guessed the word:", word)
            print("Final Score:", score)
            break

        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet.")
            continue

        if guess in guessed_letters:
            print("You already guessed this letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct Guess!")
            score += 10
        else:
            attempts -= 1
            print("❌ Wrong Guess!")

    if attempts == 0:
        print(hangman_stages[0])
        print("\n💀 GAME OVER!")
        print("Correct Word:", word)
        print("Final Score:", score)

    again = input("\nDo you want to play again? (y/n): ").lower()

    if again != "y":
        print("\n====================================")
        print("Thank You for Playing Hangman!")
        print("====================================")
        break