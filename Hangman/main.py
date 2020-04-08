# Hangman Activity
import random

word_list = ['python', 'java', 'kotlin', 'javascript']
chosen_word = random.choice(word_list)
word_list = list(chosen_word)
letters_guessed = []
preview_list = []
word_set = set(chosen_word)


def guess_check(g):
    if len(g) != 1:
        return "You should print a single letter"
    elif not g.islower():
        return "It is not an ASCII lowercase letter"
    else:
        return "True"


for x in word_list:
    preview_list.append("-")

print("H A N G M A N")
while True:
    play_check = input('Type "play" to play the game, "exit" to quit: ')
    if play_check == "play":
        fault = 0
        while fault < 8:
            if "-" in preview_list:
                print("\n")
                print("".join(preview_list))
                guess = input("Input a letter: ")
                if guess_check(guess) == "True":
                    if guess in letters_guessed:
                        print("You already typed this letter")
                    elif guess in word_set:
                        i = 0
                        while i < len(chosen_word):
                            if chosen_word[i] == guess:
                                preview_list[i] = guess
                                letters_guessed.append(guess)
                                i += 1
                            else:
                                i += 1
                    else:
                        print("No such letter in the word")
                        fault += 1
                        letters_guessed.append(guess)
                else:
                    print(guess_check(guess))
            else:
                print("\n")
                print("".join(preview_list))
                print("You guessed the word!")
                print("You survived!")
                break
        else:
            print("You are hanged!")
    elif play_check == "exit":
        break
    else:
        continue
