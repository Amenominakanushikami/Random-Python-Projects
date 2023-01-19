import random
import string
import nltk

nltk.download('words')
words = nltk.corpus.words.words()
word_list = words[:1000]

def hangman():
    word = random.choice(word_list)
    guessed_letters = []
    incorrect_guesses = 0
    while incorrect_guesses < 6:
        guess = input("Guess a letter: ")
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif not guess.isalpha() or len(guess) > 1 or guess.isspace():
            print("Invalid input, please enter a single letter")
        elif guess in word:
            guessed_letters.append(guess)
            print(" ".join([letter if letter in guessed_letters else "_" for letter in word]))
            if "_" not in " ".join([letter if letter in guessed_letters else "_" for letter in word]):
                print("You Win!")
                break
        else:
            incorrect_guesses += 1
            print("Incorrect. You have", 6 - incorrect_guesses, "guesses left.")
    if incorrect_guesses == 6:
        print("You lose")
        print(word)
    replay = input("Enter Yes to play again!: ").lower()
    if replay == "yes":
        hangman()
    else:
        print("See ya next time!")

hangman()