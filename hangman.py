import random

wordslist = [
    'correction', 'childish', 'beach', 'python', 'assertive',
    'interference', 'complete', 'share', 'credit card', 'rush', 'south'
]

word = random.choice(wordslist).lower()

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

while True:
    display_word = ""

    for letter in word:
        if letter == " ":
            display_word += " "
        elif letter in guessed_letters:
            display_word += letter
        else:
            display_word += "*"

    print("\nWord:", display_word)
    print("Guessed letters:", guessed_letters)
    print("Wrong guesses left:", max_wrong_guesses - wrong_guesses)

    if "*" not in display_word:
        print("You won!")
        break

    if wrong_guesses == max_wrong_guesses:
        print("You lost!")
        print("The word was:", word)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter only.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")