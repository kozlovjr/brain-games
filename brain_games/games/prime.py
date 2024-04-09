import prompt
from brain_games.get_random_num import get_random_num

description = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def is_prime(num): 
    limit = round(num / 2) + 1

    dividers = []
    
    for item in range(1, limit):
        if num % item == 0:
            dividers.append(item)
        
        if len(dividers) > 2:
            return 'no'
    
    return 'yes'

def prime_game():
    num = get_random_num()
    print(f"Question: {num}")

    correct_answer = is_prime(num)
    user_answer = prompt.string("Your answer: ")

    return [correct_answer, user_answer]