#! /usr/bin/env python3
# coding: utf-8

import csv
from time import time

MAX_VALUE_INVEST = 500


def recuperation_information(csv_import):
    """
    function to retrieve information related to the stock
    :param csv_import: the file contains list of actions with header : name, price and profit
    :return: a dictionnary contains all actions present in the csv file
    """
    dict_action = {}
    with open(csv_import, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if 0 < float(row['price']) <= 500:
                dict_action[row['name']] = {
                    'price': float(row['price']),
                    'profit': float(row['profit']),
                    'euros': round(float(row['price']) * float(row['profit']) / 100, 2)
                }
    dict_action = sorted(dict_action.items(), key=sort_by_profit)
    return dict_action


def sort_by_profit(x):
    """
    sort by profit (in percent)
    :param x:
    :return: a sorted list of actions
    """
    return [-x[1]['profit'], -x[1]['price']]


def sort_by_price(x):
    """
        sort by price (in euros)
        :param x:
        :return: a sorted list of actions
        """
    return [-x[1]['price'], -x[1]['profit']]


def sort_by_euros(x):
    """
        sort by price (in euros)
        :param x:
        :return: a sorted list of actions
        """
    return [-x[1]['euros'], -x[1]['profit']]


def calc_best_rendement(dict_action):
    invest = 0
    profit = 0
    list_actions = []
    result = []
    for action in dict_action:
        test = invest + action[1]['price']
        if test <= MAX_VALUE_INVEST:
            invest = invest + action[1]['price']
            list_actions.append(action[0])
            profit = profit + action[1]['euros']

    result.append((list_actions, round(invest, 2), round(profit, 2)))

    return result


def best_return(result):
    profit = round(result[0][2] / result[0][1] * 100, 2)
    return profit


if __name__ == '__main__':
    time1 = time()
    dict_actions_profit = recuperation_information('data_20_actions.csv')
    dict_actions_price = sorted(dict_actions_profit, key=sort_by_price)
    dict_actions_euros = sorted(dict_actions_profit, key=sort_by_euros)
    result_profit = calc_best_rendement(dict_actions_profit)
    result_price = calc_best_rendement(dict_actions_price)
    result_euros = calc_best_rendement(dict_actions_euros)

    list_return = []
    return_profit = best_return(result_profit)
    return_price = best_return(result_price)
    return_euros = best_return(result_euros)

    list_return.append(return_profit)
    list_return.append(return_price)
    list_return.append(return_euros)

    best_solution = max(list_return)
    print(best_solution)
    if best_solution == return_profit:
        print(result_profit)
    elif best_solution == return_price:
        print(result_price)
    else:
        print(result_euros)

    time2 = time() - time1
    print(f'\nExecution : {time2}s')
