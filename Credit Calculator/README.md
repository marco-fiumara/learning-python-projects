## [learning-python-projects](https://github.com/marco-fiumara/learning-python-projects)

# Credit Calculator: Intermediate

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
2.

- you must only choose one of either `diff` or `annuity`,
- you must only choose two of `--principal`, `--periods` and `--payment`,
- `--interest` must be included
- therefore you should have a total of 4 arguments (The order you put them in does not matter)

3. no values can be negative,
4. if you select `diff` as a type, you cannot also have `--payment`, as diff calculates differentiated payments for each period

Any violations will result in a message of `Incorrect parameters`

### Examples:

The following is an example interaction of a user using the program.

(NOTE: The `>` you see is not included in the program, but indicates where the user has inputted information)

**Example 1:** _find an annuity payment for the 60-month (or 5-year) credit with the principal 1,000,000 and 10% interest_

```
> python main.py --type=annuity --principal=1000000 --periods=60 --interest=10
Your annuity payment = 21248!
Overpayment = 274880
```

**Example 2:** _less than 4 arguments are given_

```
> python main.py --type=diff --principal=1000000 --payment=104000
Incorrect parameters.
```

**Example 3:** _calculate differentiated payments given the principal 500,000, the period of 8 months and the interest rate 7.8%_

```
> python main.py --type=diff --principal=500000 --periods=8 --interest=7.8
Month 1: paid out 65750
Month 2: paid out 65344
Month 3: paid out 64938
Month 4: paid out 64532
Month 5: paid out 64125
Month 6: paid out 63719
Month 7: paid out 63313
Month 8: paid out 62907

Overpayment = 14628
```

**Example 4:** _calculate the principal for a user paying 8,722 per month for 120 months (10 years) with the interest 5.6%_

```
> python main.py --type=annuity --payment=8722 --periods=120 --interest=5.6
Your credit principal = 800018!
Overpayment = 246622
```

**Example 5:** _figure out how much time a user needs to repay the credit with 500,000 principal, 23,000 monthly payment and 7.8% interest_

```
> python main.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
You need 2 years to repay this credit!
Overpayment = 52000
```
