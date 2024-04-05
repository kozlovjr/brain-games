from brain_games.cli import welcome_user

def main(description, round):
    print("Welcome to the Brain Games!")

    name = welcome_user()
    
    print(description)

    count_round = 1

    while count_round <= 3:
        [correct_answer, user_answer] = round()

        if correct_answer != user_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        
        print("Correct!")

        count_round += 1
    
    print(f"Congratulations, {name}!")