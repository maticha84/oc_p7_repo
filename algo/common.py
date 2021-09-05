#! /usr/bin/env python3
# coding: utf-8

from csv import DictReader
from os import path, remove

def retrieve_information(csv_import, bruteforce=False):
    """
    function to retrieve information related to the stock
    :param bruteforce: boolean to indicate if bruteforce or not
    :param csv_import: the file contains list of actions with header : name, price and profit
    :return: a list contains all actions present in the csv file
    """
    list_actions = []
    end = False
    try:
        with open(csv_import, 'r') as csv_file:
            reader = DictReader(csv_file)

            for row in reader:
                profit_euros = float(row['profit']) * float(row['price']) / 100
                price = float(row['price'])
                if not bruteforce:
                    if price > 0 and profit_euros > 0:  # don't take into account losses
                        list_actions.append((row['name'], price, profit_euros))
                else:
                    list_actions.append((row['name'], price, profit_euros))  # all possibilities
        list_actions = sorted(list_actions, key=sort_by_profit)
    except KeyError:
        print(f"The file {csv_import} must be a csv file, with header : 'name, price, profit'\n")
        end = True
        list_actions = [0, 0]
    if not list_actions:
        print(f"The file {csv_import} is empty.\n")
        end = True
    return list_actions, end


def sort_by_profit(x):
    """
    sort by profit (in percent)
    :param x:
    :return: a sorted list of actions
    """
    return [-x[2], -x[1]]


def result_export(choice, action_selection, total_invest, total_profit):
    if path.exists(f'./results/{choice}.txt'):
        remove(f'./results/{choice}.txt')

    result_for_file = ""
    for action in action_selection:
        result_for_file += f"{action[0]:<10} -- price : {action[1]:>6.2f} € -- profit : {action[2]:>6.2f} €\n"

    with open(f'./results/{choice}.txt', 'xt') as result_file:
        result_file.write(f"\nBest choice to invest : \n\n"
                          f"{result_for_file}"
                          f"\nTotal cost: {total_invest:>6.2f} € \n"
                          f"Total return: {total_profit:>6.2f} €\n\n")
