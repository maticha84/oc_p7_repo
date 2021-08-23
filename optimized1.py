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
    dict_action = sorted(dict_action.items(), key=lambda x: x[1]['profit'], reverse=True)
    return dict_action


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

    result.append((list_actions, invest, profit))

    return result


if __name__ == '__main__':
    time1 = time()
    dict_actions = recuperation_information('data_20_actions.csv')

    result = calc_best_rendement(dict_actions)
    print(result)
    time2 = time() - time1
    print(f'\nExecution : {time2}s')
