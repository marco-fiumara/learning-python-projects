import math
import sys
from methods import args_checker, annuity, diff

args = sys.argv[1:]

numbers = args_checker(args)

if numbers == 'error':
    print("Incorrect parameters")
else:
    set_type = numbers['type']
    if set_type == 'annuity':
        annuity(numbers)
    elif set_type == 'diff':
        diff(numbers)
