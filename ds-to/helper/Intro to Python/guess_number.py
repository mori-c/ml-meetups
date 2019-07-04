"""
Author: Ted Petrou
Purpose: This program attempts to guess a users number between 1 and 1000
"""
import random
from collections import namedtuple

def validate_number(num, low, high):
    """
    Takes user input as a string and validates that it is 
    an integer between low and high
    """
    try:
        num = int(num)
    except ValueError:
        return False

    if num < low or num > high:
        return False
    return True

def check_guess(guess):
    """
    Asks user if guess is correct
    """
    answer = ''

    while answer not in ['n', 'y']:
        answer = input(f'Is your numer {guess} (y/n)? ')

    if answer == 'y':
        print('I guessed your number!')
        exit()

def get_digits(num):
    """
    Creates a list of the digits of num
    """
    return [int(d) for d in str(num)]

def get_sum_digits(num):
    """
    Sums all digits of num
    """
    return sum(get_digits(num))

def get_digit_range(num):
    """
    Subtracts the largest and smallest digit
    """
    digits = get_digits(num)
    return max(digits) - min(digits)

def get_digit_prod(num):
    """
    Multiplies the largest two digits of num together
    """
    digits = sorted(get_digits(num))[-2:]
    prod = 1
    for d in digits:
        prod *= d
    return prod

def has_possible_values(pv):
    if len(pv) == 0:
        print('Something went wrong. There are no numbers left to guess :(')
        exit()

# Make list of all possible values
possible_values = list(range(1, 1001))

# Introduction
print('\n\nWelcome to Guess your Number game!')
name = input('Please enter your name: ')
print(f'\nNice to meet you {name}!')

print('Think of a number between 1 and 1000 for me to guess.')
input('Press enter when you are ready to continue ')

# Create 'database' of questions
Question = namedtuple('Question', ['question', 'min', 'max', 'function'])

q1 = Question('\nWhat is the sum of the digits? ', 1, 27, get_sum_digits)
q2 = Question('\nWhat is absolute difference between the maximum and minimum digits? ', 0, 9, get_digit_range)
q3 = Question('\nWhat is the product of the two largest digits? ', 0, 81, get_digit_prod)

questions = [q1, q2, q3]

# Run main game logic
for question in questions:
    input_value = -999
    while not validate_number(input_value, question.min, question.max):
        input_value = input(question.question)
    input_value = int(input_value)
    possible_values = [x for x in possible_values if question.function(x) == input_value]
    has_possible_values(possible_values)
    guess = random.choice(possible_values)
    check_guess(guess)
    possible_values.remove(guess)

# Make one final guess
final_guess = possible_values[0]
print('\nOk one final guess')
check_guess(final_guess)
possible_values.remove(final_guess)
has_possible_values(possible_values)

# End game
if len(possible_values) == 1:
    print('\nIt must be ', possible_values[0], '!')
else:
    print('\nI give up!')
    print('These are the numbers that are left: ', possible_values)
