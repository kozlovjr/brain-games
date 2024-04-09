import prompt
import random
from brain_games.get_random_num import get_random_num

description = "What number is missing in the progression?"

def progression_game():
    factors = ('+', '-')

    first_num = get_random_num()
    difference = get_random_num()
    factor = random.choice(factors)

    job = [first_num] 

    while len(job) <= 10:
        if factor == '+':
            last_num = job[-1] + difference
            job.append(last_num)
        else:
            last_num = job[-1] - difference
            job.append(last_num)
    
    random_index = random.randint(0, len(job) - 1)
    correct_answer = job[random_index]

    job[random_index] = '..'

    question = f"Question: {' '.join(map(str,job))}"

    print(question)

    user_answer = prompt.integer("Your answer: ")

    return [correct_answer, user_answer]

