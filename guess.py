import random

print("""These are the rules of the game:
      Objective: Guess the word one letter at a time
      Every correct letter guessed will be revealed
      After 10 incorrect guesses, the game will end. """)

word_list = ["sunset", "giraffe", "whisper", "zephyrs", "journey", "victory", "explore", "chimney", "blanket", "freedom"]

chosen = random.choice(word_list)
wordlen = len(chosen)


guessed_word = ["-"] * wordlen
incorrect_guesses = 0   

print("Welcome to the Guessing Game!")
client_name = input("Please enter your name: ")
print("Good luck, " + client_name + "!")

while incorrect_guesses < 10:
    print(" ".join(guessed_word))
    guess = input('Guess a single letter: ').lower()

    if guess in chosen:
        for i in range(wordlen):
            if chosen[i] == guess:
                guessed_word[i] = guess
        if "-" not in guessed_word:
            print(" ".join(guessed_word))
            print("Congratulations, you've guessed the word correctly!")
            print("You won. Congrats, " + client_name + "!")
            break
    else:
        incorrect_guesses += 1
        remaining_guesses = 10 - incorrect_guesses
        print(f"Letter not found. You have {remaining_guesses} guesses left.\n")

if "-" in guessed_word:
    print("You lost. The correct word was: " + chosen)
    print("Better luck next time, " + client_name + ".")