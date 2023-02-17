import prompt
from brain_games.cli import welcome_user


def launch_game(game):
    print('Welcome to the Brain Games!')
    username = welcome_user()
    print(game.RULE)
    for i in range(1, 4):
        question, correct_answer = \
            game.generate_question_n_answer()
        answer = prompt.string(f'Question: {question}\nYour answer: ')
        if answer == str(correct_answer):
            print('Correct!')
        else:
            print(f"'{answer}' is a wrong answer ;("
                  f". Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {username}!")
            break
        if i == 3:
            print(f'Congratulations, {username}!')
