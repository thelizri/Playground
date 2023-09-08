import numpy as np
from numpy import random


def is_winning(number):
    if number <= 10 or number >= 45:
        return True
    return False


def throw_dice():
    dice_sum = 0
    dice_sum += random.randint(1, 5)
    dice_sum += random.randint(1, 7)
    dice_sum += random.randint(1, 9)
    dice_sum += random.randint(1, 13)
    dice_sum += random.randint(1, 21)
    return dice_sum


number_of_trials = 20_000
winning_games = 0
for i in range(number_of_trials):
    dice_sum = throw_dice()
    if is_winning(dice_sum):
        winning_games += 1

print(f"Probability of winning is {winning_games/number_of_trials}")

# Probability (500 trials): 1%
# Probability (1 000 trials): 1.2%
# Probability (10 000 trials): 0.83%
# Probability (100 000 trials): 1.064%
# Probability (500 000 trials): 1.0884%
# Probability (1000 000 trials): 1.0668%
