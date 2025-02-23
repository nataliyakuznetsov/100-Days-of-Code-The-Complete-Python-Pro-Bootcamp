import random
from hangman_words import word_list
from hangman_art import logo, stages

# logo
print(logo)

# the randomly chosen word
chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)

# creation of the placeholder
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
# list for holding correct guessed letters
correct_letters = []

# number of lives
lives = 6

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    # receiving the letter from the user
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    # conditions when guessed letter is in the word
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess) # add letter to correct_letters
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

   #  if guessed letter is not in the word

    if guess not in chosen_word:
        lives -= 1  # lose life
        print(f"You guess {guess}, that's not in the world. You lose the life.")
        
        # game over and lose
        if lives == 0:
            game_over = True

            print(f"***********************IT WAS {chosen_word.upper()}! YOU LOOSE**********************")
    # game over and win
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
