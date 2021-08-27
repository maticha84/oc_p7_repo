#! /usr/bin/env python3
# coding: utf-8

import csv
from time import time

MAX_VALUE_INVEST = 500


def recuperation_information(csv_import):
    """
    function to retrieve information related to the stock
    :param csv_import: the file contains list of actions with header : name, price and profit
    :return: a list contains all actions present in the csv file
    """
    list_actions = []
    with open(csv_import, 'r') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            profit_euros = round(float(row['profit'])*float(row['price'])/100, 2)
            list_actions.append((row['name'], float(row['price']), profit_euros))

    return list_actions


def bruteforce(list_actions, max_value=MAX_VALUE_INVEST, actions_selection=[]):
    """

    :param list_actions: a list
    :param max_value:by default, MAX_VALUE_INVEST
    :param actions_selection: for return a list of actions whose respect constraints
    :return: the list of best invest actions
    """

    if list_actions:
        action1, list_action1 = bruteforce(list_actions[1:], max_value, actions_selection)
        action = list_actions[0]

        if action[1] <= max_value:
            action2, list_action2 = bruteforce(list_actions[1:], max_value - action[1], actions_selection + [action])
            if action1 < action2:
                return action2, list_action2

        return action1, list_action1
    else:
        return round(sum([i[2] for i in actions_selection]),2), actions_selection


if __name__ == "__main__":

    time1 = time()

    list_actions = recuperation_information('data_20_actions.csv')

    result = bruteforce(list_actions)

    print(f"Maximum profit in euros : {str(result[0])} euros\n\n"
          f"Best choice to invest : \n")
    for i in range(0, len(result[1])):
        print(f"{result[1][i][0]} -- price : {result[1][i][1]} € -- profit : {result[1][i][2]} € ")
    total_invest = round(sum(i[1] for i in result[1]))
    print(f"\nTotal invest = {total_invest} € \n")

    final_time = time() - time1
    print(f"Execution time : {final_time} seconds")
