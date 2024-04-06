import prompt
from random import choice 
from brain_games.get_random_num import get_random_num

description = 'What is the result of the expression?'

def calc_game():
    first_num = get_random_num()
    second_num = get_random_num()

    expressions = ['+', '-', '*']
    expression = choice(expressions)

    print(f"Question: {first_num} {expression} {second_num}")

    user_answer = prompt.integer('Your answer: ')

    if expression == '+':
        correct_answer = first_num + second_num
        return [correct_answer, user_answer]
    if expression == '-':
        correct_answer = first_num - second_num
        return [correct_answer, user_answer]
    if expression == '*':
        correct_answer = first_num * second_num 
        return [correct_answer, user_answer]