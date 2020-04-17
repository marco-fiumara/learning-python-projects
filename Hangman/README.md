## [learning-python-projects](https://github.com/marco-fiumara/learning-python-projects)

# Hangman activity: Easy

Games can help you kill time when you’re bored. But before smartphones, people played games the classic way – with paper and pencil. Let’s recreate one such game and improve your programming skills in the process. In this project, you will code Hangman, a game where the player has to guess a word, letter by letter, in a limited number of attempts. Make a program that plays Hangman with you – and good luck with the guessing!

### The Hangman activity helped to reinforce the basic concepts, such as:

- elif statements
- tuples
- default parameters
- random module
- math module
- for loop
- loop control statements (break, continue, loop else, if !=)
- reading errors & stack trace

### Instructions:

Open up terminal and `cd` into the directory containing the 'Hangman' folder and run `python main.py`

The program selects a random word from a list of programming languages (python, java, kotlin and javascript).

You will then start guessing potential letters in the unknown word, with a limit of 8 incorrect guesses.

### Example:

The following is an example interaction of a user using the program.

(NOTE: The `>` you see is not included in the program, but indicates where the user has inputted information)

```
H A N G M A N
Type "play" to play the game, "exit" to quit: > play

----------
Input a letter: > a

-a-a------
Input a letter: > i

-a-a---i--
Input a letter: > o
No such letter in the word

-a-a---i--
Input a letter: > o
You already typed this letter

-a-a---i--
Input a letter: > p

-a-a---ip-
Input a letter: > p
You already typed this letter

-a-a---ip-
Input a letter: > h
No such letter in the word

-a-a---ip-
Input a letter: > k
No such letter in the word

-a-a---ip-
Input a letter: > a
You already typed this letter

-a-a---ip-
Input a letter: > z
No such letter in the word

-a-a---ipt
Input a letter: > t

-a-a---ipt
Input a letter: > x
No such letter in the word

-a-a---ipt
Input a letter: > b
No such letter in the word

-a-a---ipt
Input a letter: > d
No such letter in the word

-a-a---ipt
Input a letter: > w
No such letter in the word
You are hanged!

Type "play" to play the game, "exit" to quit: > exit
```
