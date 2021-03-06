#! /usr/bin/env python3
# coding: utf-8
"""
This optimised version will calculate the best choice of shares to obtain the best return,
while maintaining the constraint of a maximum investment value (MAX_VALUE_INVEST).
Optimised version using matrix calculation.
This is called the dynamic backpack algorithm.
"""
from algo.common import retrieve_information, result_export
from time import time
import re

MAX_VALUE_INVEST = 500


def dynamic_search(list_actions, max_value=MAX_VALUE_INVEST):
    """
    :param list_actions: a list contains all positives actions
    don't take account into losses
    :param max_value: MAX_VALUE_INVEST - integer type
    :return:
    matrix[-1][-1] : a float corresponding profits
    actions_selection : a list corresponding all action selected taking account constraints
    max_invest : a float corresponding max invest under MAX_VALUE_INVEST
    """
    matrix = [[0 for x in range(max_value + 1)] for x in range(len(list_actions) + 1)]

    for i in range(1, len(list_actions) + 1):
        for wallet in range(1, max_value + 1):
            if list_actions[i - 1][1] <= wallet:
                matrix[i][wallet] = max(list_actions[i - 1][2] + matrix[i - 1][int(wallet - list_actions[i - 1][1])],
                                        matrix[i - 1][wallet])  # choose the best value
            else:
                matrix[i][wallet] = matrix[i - 1][wallet]

    wallet = max_value
    nb_actions = len(list_actions)
    actions_selection = []

    while wallet >= 0 and nb_actions >= 0:
        action = list_actions[nb_actions - 1]
        if matrix[nb_actions][int(wallet)] == matrix[nb_actions - 1][int(wallet - action[1])] + action[2]:
            actions_selection.append(action)
            wallet -= action[1]

        nb_actions -= 1

    max_invest = MAX_VALUE_INVEST - wallet
    return matrix[-1][-1], actions_selection, max_invest


def run_optimized(csv_file):
    """
    :param csv_file: csv file contains all actions to consider
    :return: list of best actions, total cost and total return
    """
    start_time = time()

    match = re.search('/(\\w+)\\.csv', csv_file)
    nom_file = f'optimized_{match.group(1)}'

    list_action, fin = retrieve_information(csv_file)
    if not fin:
        max_profit, action_selection, max_invest = dynamic_search(list_action)

        print("\nBest choice to invest : \n")

        for action in action_selection:
            print(f"{action[0]:<10} -- price : {action[1]:>6.2f} ??? -- profit : {action[2]:>6.2f} ??? ")

        print(f"\nTotal cost: {max_invest:>6.2f} ??? \n"
              f"Total return: {max_profit:>6.2f} ???\n\n")

        result_export(nom_file, action_selection, max_invest, max_profit)

        end_time = time() - start_time
        print(f'Execution time : {end_time} seconds\n')


if __name__ == '__main__':
    run_optimized('../csv/dataset2.csv')
