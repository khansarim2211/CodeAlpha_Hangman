import random

def hangman():
    # List of predefined words
    words = ["python", "java", "javascript", "php", "ruby"]
    word = random.choice(words)
    word_letters = set(word)  # Set of letters in the chosen word
    guessed_letters = set()   # Letters guessed by player
    incorrect_guesses = 0
    max_incorrect = 6

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters: {'_ ' * len(word)}")

    while incorrect_guesses < max_incorrect and word_letters != guessed_letters:
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

        # Get player input
        guess = input("Guess a letter: ").lower()
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

    # Game over
    if word_letters == guessed_letters:
        print(f"\nCongratulations! You guessed the word: {word}")
    else:
        print(f"\nGame Over! The word was: {word}")

# Start the game
hangman()