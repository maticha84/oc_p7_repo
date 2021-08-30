#! /usr/bin/env python3
# coding: utf-8

from algo_package.common import recuperation_information
from time import time

MAX_VALUE_INVEST = 500


def bruteforce(list_actions, max_value=MAX_VALUE_INVEST, actions_selection=None):
    """

    :param list_actions: a list
    :param max_value:by default, MAX_VALUE_INVEST
    :param actions_selection: for return a list of actions whose respect constraints
    :return: sum([i[2] for i in actions_selection]) : the maximum invest
             actions_selection : the list of best invest actions
    """

    if actions_selection is None:
        actions_selection = []

    if list_actions:
        profit_action1, list_action1 = bruteforce(list_actions[1:],
                                                  max_value,
                                                  actions_selection
                                                  )
        action = list_actions[0]
        if action[1] <= max_value:
            profit_action2, list_action2 = bruteforce(list_actions[1:],
                                                      max_value - action[1],
                                                      actions_selection + [action]
                                                      )
            if profit_action1 < profit_action2:
                return profit_action2, list_action2

        return profit_action1, list_action1
    else:
        return sum([i[2] for i in actions_selection]), actions_selection


def run_bruteforce(csv_file):
    time1 = time()

    list_actions, fin = recuperation_information(csv_file)
    if not fin:
        result = bruteforce(list_actions)

        print(f"\nBest choice to invest : \n")
        for i in range(0, len(result[1])):
            print(f"{result[1][i][0]:<10} -- price : {result[1][i][1]:>6.2f} € -- profit : {result[1][i][2]:>6.2f} € ")
        total_invest = round(sum(i[1] for i in result[1]))
        print(f"\nTotal invest = {total_invest:>6.2f} € \n"
              f"Maximum profit in euros : {result[0]:>6.2f} euros\n")

        final_time = time() - time1
        print(f"Execution time : {final_time} seconds\n")


if __name__ == "__main__":
    run_bruteforce('../data_20_actions.csv')
