import prompt
from brain_games.get_random_num import get_random_num

description = 'Answer "yes" if the number is even, otherwise answer "no".'

def even_game():
    num = get_random_num()
    print(f"Question: {num}")
    correct_answer = 'yes' if num % 2 == 0 else 'no'
    user_answer = prompt.string('Your answer: ')

    return [correct_answer, user_answer]