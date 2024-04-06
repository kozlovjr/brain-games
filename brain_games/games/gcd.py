import prompt
from brain_games.get_random_num import get_random_num

description = "Find the greatest common divisor of given numbers."

def get_gcd(first_num, second_num):
    if first_num < second_num:
        second_num, first_num = first_num, second_num
    
    if first_num % second_num == 0:
        return second_num
    
    return get_gcd(second_num, first_num % second_num)

def game_gcd():
    first_num = get_random_num()
    second_num = get_random_num()

    print(f"Question: {first_num} {second_num}")

    user_answer = prompt.integer("Your answer: ")
    correct_answer = get_gcd(first_num, second_num)

    return [correct_answer, user_answer]