## learning-python-projects

# Credit Calculator activity: Intermediate

Finance is an important part of the life of any people. Sometimes you think about getting additional income and want to open a deposit account. And sometimes you need additional money right now and want to take a credit or mortgage. Anyway, you may want to calculate different financial indicators to make a decision. Let’s make such an instrument that can help us.

### The Credit Calculator activity helped to reinforce the basic concepts, such as:

- math module
- terminal / command line
- running files and passing arguments from the terminal

### Instructions:

Open up terminal and enter the following command:
(NOTE: this command is if you are in the Credit Calculator directory in the terminal, if you aren't, you can also do this by putting the full path to (and including) the main.py file)
`python [file path / filename (incl. extension) i.e. main.py] --type=[annuity or diff] --principal=[int] --periods=[int] --interest=[int or float] --payment[int or float]`

There are rules however:

1. all arguments must have `--` before them,
2. 1. you must only choose one of either `diff` or `annuity`,
   2. you must only choose two of `--principal`, `--periods` and `--payment`,
   3. `--interest` must be included
   4. therefore you should have a total of 4 arguments (The order you put them in does not matter)
3. no values can be negative,
4. if you select `diff` as a type, you cannot also have `--payment`, as diff calculates differentiated payments for each period

Any violations will result in a message of `Incorrect parameters`

### Examples:

`python main.py --type=annuity --principal=1000000 --periods=60 --interest=10`

`python main.py --type=diff --principal=1000000 --periods=10 --interest=10`

`python main.py --type=annuity --payment=8722 --periods=120 --interest=5.6`
