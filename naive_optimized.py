#! /usr/bin/env python3
# coding: utf-8
"""
This optimisation is derived from the so-called "rucksack optimisation".
The best returns are taken into account and added to the maximum sum of 500€.
This is the 'naive algorithm'
"""
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
            profit_euros = float(row['profit']) * float(row['price']) / 100
            price = float(row['price'])
            if price > 0 and profit_euros > 0:  # don't take into account losses
                list_actions.append((row['name'], price, profit_euros))
    list_actions = sorted(list_actions, key=sort_by_profit)
    return list_actions


def sort_by_profit(x):
    """
    sort by profit (in percent)
    :param x:
    :return: a sorted list of actions
    """
    return [-x[2], -x[1]]


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
    time1 = time()

    list_actions = recuperation_information(csv_file)
    action_selection, invest, profit = calc_best_return(list_actions)

    print("\nBest choice to invest : \n")

    for action in action_selection:
        print(f"{action[0]:<10} -- price : {action[1]:>6.2f} € -- profit : {action[2]:>6.2f} € ")

    print(f"\nTotal invest = {invest:>6.2f} € \n"
          f"Maximum profit in euros : {profit:>6.2f} euros\n\n")

    time2 = time() - time1
    print(f'Execution time : {time2} seconds\n')


if __name__ == '__main__':
    run_naive_optimized('dataset2.csv')
