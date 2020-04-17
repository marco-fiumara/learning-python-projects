## [learning-python-projects](https://github.com/marco-fiumara/learning-python-projects)

# Tic-Tac-Toe: Easy

Everybody remembers this paper-and-pencil game from childhood: Tic-Tac-Toe, also known as Noughts and crosses or Xs and Os. A single mistake usually costs you the game, but thankfully it is simple enough that most players discover the best strategy quickly. Let’s program Tic-Tac-Toe and get playing!

### The Tic-Tac-Toe activity helped to reinforce the basic concepts, such as:

- list comprehension
- nested lists
- any()
- all()
- basic error handling (try, except)

### Instructions:

Open up terminal and `cd` into the directory containing the 'Tic-Tac-Toe' folder and run `python main.py`

The program will draw a box, which represents a 3x3 grid.

The grid works through the user entering coordinates. The first move is always 'X', and both 'X' and 'O' are controlled by the user.

The coordinates are as follows:

(1,3) (2,3) (3,3)
(1,2) (2,2) (3,2)
(1,1) (2,1) (3,1)

Coordinates should be seperated by a space.

Combinations work the same as normal tic-tac-toe, with three matching options in a row, column or diagonal.

### Example:

The following is an example interaction of a user using the program.

(NOTE: The `>` you see is not included in the program, but indicates where the user has inputted information)

```
---------
|       |
|       |
|       |
---------
Enter the coordinates: > 2 2
---------
|       |
|   X   |
|       |
---------
Enter the coordinates: > 2 2
This cell is occupied! Choose another one!
Enter the coordinates: > two two
You should enter numbers!
Enter the coordinates: > 1 4
Coordinates should be from 1 to 3!
Enter the coordinates: > 1 3
---------
| O     |
|   X   |
|       |
---------
Enter the coordinates: > 3 1
---------
| O     |
|   X   |
|     X |
---------
Enter the coordinates: > 1 2
---------
| O     |
| O X   |
|     X |
---------
Enter the coordinates: > 1 1
---------
| O     |
| O X   |
| X   X |
---------
Enter the coordinates: > 3 2
---------
| O     |
| O X O |
| X   X |
---------
Enter the coordinates: > 2 1
---------
| O     |
| O X O |
| X X X |
---------
X wins
```
