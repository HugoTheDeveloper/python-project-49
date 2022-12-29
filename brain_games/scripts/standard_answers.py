#!/usr/bin/env python3
from brain_games.cli import name_list


def is_answer_correct(answer, correct_answer):
    if answer == correct_answer:
        print('Correct!')
    else:
        print(f"'{answer}' is a wrong answer ;(. \
        Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name_list[0]}!")
        return True


def congratulate_user(i):
    if i == 3:
        print(f'Congratulations, {name_list[0]}!')
