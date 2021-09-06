#! /usr/bin/env python3
# coding: utf-8
"""
This optimisation is derived from the so-called "rucksack optimisation".
The best returns are taken into account and added to the maximum sum of 500€.
This is the 'naive algorithm'
"""
from algo.common import retrieve_information, result_export
from time import time
import re

MAX_VALUE_INVEST = 500


def calc_best_return(list_action):
    invest = 0
    profit = 0
    list_actions = []
    for action in list_action:
        test = invest + action[1]
        if test <= MAX_VALUE_INVEST:
            invest = invest + action[1]
            list_actions.append(action)
            profit = profit + action[2]

    return list_actions, invest, profit


def run_naive_optimized(csv_file):
    """
    :param csv_file: csv file contains all actions to consider
    :return: list of best actions, total cost and total return
    """
    start_time = time()

    match = re.search('/(\\w+)\\.csv', csv_file)
    nom_file = f'naive_optimized_{match.group(1)}'

    list_actions, fin = retrieve_information(csv_file)
    if not fin:
        action_selection, invest, profit = calc_best_return(list_actions)

        print("\nBest choice to invest : \n")

        for action in action_selection:
            print(f"{action[0]:<10} -- price : {action[1]:>6.2f} € -- profit : {action[2]:>6.2f} € ")

        print(f"\nTotal cost: {invest:>6.2f} € \n"
              f"Total return: {profit:>6.2f} €\n\n")

        result_export(nom_file, action_selection, invest, profit)

        end_time = time() - start_time
        print(f'Execution time : {end_time} seconds\n')


if __name__ == '__main__':
    run_naive_optimized('../csv/dataset2.csv')
