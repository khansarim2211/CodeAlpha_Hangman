import random

def hangman():
    # List of predefined words
    words = ["python", "java", "javascript", "php", "ruby"]
    word = random.choice(words)
    word_letters = set(word)  # Set of letters in the chosen word
    guessed_letters = set()   # Letters guessed by player
    incorrect_guesses = 0
    max_incorrect = 6

    # ASCII art for Hangman (optional improvement)
    hangman_art = [
        """
         ------
         |    |
              |
              |
              |
              |
        ==========""",
        """
         ------
         |    |
         O    |
              |
              |
              |
        ==========""",
        """
         ------
         |    |
         O    |
         |    |
              |
              |
        ==========""",
        """
         ------
         |    |
         O    |
        /|    |
              |
              |
        ==========""",
        """
         ------
         |    |
         O    |
        /|\\   |
              |
              |
        ==========""",
        """
         ------
         |    |
         O    |
        /|\\   |
        /     |
              |
        ==========""",
        """
         ------
         |    |
         O    |
        /|\\   |
        / \\   |
              |
        =========="""
    ]

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters: {'_ ' * len(word)}")

    while incorrect_guesses < max_incorrect:
        print(hangman_art[incorrect_guesses])  # Display Hangman art
        print(f"\nIncorrect guesses: {incorrect_guesses}/{max_incorrect}")
        print("Guessed letters:", ' '.join(sorted(guessed_letters)))
        
        # Display current state of word
        display = ''
        for letter in word:
            if letter in guessed_letters:
                display += letter + ' '
            else:
                display += '_ '
        print("Word:", display)

        # Check win condition early
        if word_letters.issubset(guessed_letters):
            print(f"\nCongratulations! You guessed the word: {word}")
            return True

        # Get player input
        guess = input("Guess a letter: ").lower().strip()
        if not guess:
            print("Please enter a letter!")
            continue
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print("Wrong guess!")

    # Game over (loss)
    print(hangman_art[incorrect_guesses])  # Show final state
    print(f"\nGame Over! The word was: {word}")
    return False

def play_hangman():
    while True:
        hangman()
        play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Start the game
play_hangman()
