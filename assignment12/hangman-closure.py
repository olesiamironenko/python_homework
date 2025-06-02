# Task 4: Closure Practice
# 4.2: Declare a function called make_hangman() that has one argument called secret_word
def make_hangman(secret_word):
    # 4.2: declare an empty array called guesses
    guesses = []

    #  4.2: Within the function declare a function called hangman_closure() that takes one argument, which should be a letter
    def hangman_closure(letter):
        # 4.2: each time hangman_closure is called, the letter should be appended to the guesses array
        guesses.append(letter)
        display_word = ""
        complete = True

        for char in secret_word:
            if char in guesses:
                display_word += char
            else:
                display_word += "_"
                complete = False

        # 4.2: Print out the word, with underscores substituted for the letters that haven't been guessed
        print("Current word:", display_word)
        return complete

    return hangman_closure
# 4.3: Within hangman-closure.py, implement a hangman game that uses make_hangman()
if __name__ == "__main__":
    # 4.3: Use the input() function to prompt for the secret word
    secret = input("Enter the secret word: ").lower()
    
    guess_func = make_hangman(secret)

    print("Let's play Hangman!\n")

    while True:
        # 4.3: Use the input() function to prompt for each of the guesses, until the full word is guessed
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess_func(guess):
            print(f"Congratulations! You've guessed the word: {secret}")
            break