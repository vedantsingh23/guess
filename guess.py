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

while incorrect_guesses < 10:
    guess = input('Guess a single letter: ').lower()
    if guess in chosen:
        for i in range(wordlen):
            if chosen[i] == guess:
                guessed_word[i] = guess
    
                
