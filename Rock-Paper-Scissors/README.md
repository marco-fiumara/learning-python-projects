## [learning-python-projects](https://github.com/marco-fiumara/learning-python-projects)

# Rock-Paper-Scissors: Intermediate

If you’ve ever wanted to create games, this project will get you started! In this project you will code a Rock-Paper-Scissors-Lizard-Spock game, a more advanced version of Rock-Paper-Scissors, which can be played against the computer.

### The Rock-Paper-Scissors activity helped to reinforce the basic concepts, such as:

- opening files
- reading files
- overwriting files
- appending information / updating files
- print() sep and end
- string slicing

### Instructions:

Open up terminal and `cd` into the directory containing the 'Rock-Paper-Scissors' folder and run `python main.py`

The program will prompt you to enter your name, then after greeting you, will let you input custom options.

If you do not wish to utilise custom options, you can simply press `return`.

The custom options must consist of an odd number, and will be put into a format where a selected option will loose to half the other options, and will beat the other half.

An example of this can be found [here](https://i.stack.imgur.com/xgoX1.jpg)

Playing the game consists of typing the desired option, such as `rock`.

If you beat the computer, you will receive 100 points, if you tied you will receive 50 points, and a loss will result in 0 points.

The users score will be kept throughout the execution of the program. This can be viewed when you type the `!rating` command.

Once a user runs the `!exit` command, their rating will be totalled and written to the 'rating.txt' file.

If the user restarts the program, their score will be read from the file, thus letting them continue off from where they left.

### Examples:

The following is an example interaction of a user using the program.

(NOTE: The `>` you see is not included in the program, but indicates where the user has inputted information)

**Example 1:**

```
Enter your name: > Tim
Hello, Tim
> rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire
Okay, let's start
> rock
Sorry, but computer chose air
> !rating
Your rating: 0
> rock
Well done. Computer chose sponge and failed
> !rating
Your rating: 100
> !exit
Bye!
```

**Example 2:**

```
Enter your name: > Tim
Hello, Tim
>
Okay, let's start
> rock
Well done. Computer chose scissors and failed
> paper
Well done. Computer chose rock and failed
> paper
There is a draw (paper)
> scissors
Sorry, but computer chose rock
> !exit
Bye!
```
