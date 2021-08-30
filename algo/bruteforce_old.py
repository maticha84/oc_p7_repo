#! /usr/bin/env python3
# coding: utf-8

import itertools
import csv
from tqdm import tqdm

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

        for row in tqdm(reader):
            dict_action[row['name']] = {'price': float(row['price']), 'profit': float(row['profit'])}

    return dict_action


def calculate_profit_euros(dict_action):
    """

    :param dict_action: dictionary containing all the stocks to be processed
    :return: add a key/value in the dictionnary : profit over 2 years
    """
    for action in tqdm(dict_action):
        dict_action[action]['euros'] = round(dict_action[action]['price'] * dict_action[action]['profit'] / 100, 2)


def search_all_possible_combinations(dict_action):
    """
    Allows to return a list of valid actions taking into account constraints such as :
        1 stock can only be bought once
        the maximum bet is MAX_VALUE_INVEST
    :param dict_action: dictionary containing all the stocks to be processed
    :return: possible_combinations_with_constraints (list)
    """
    action_price_euros = []
    for action in dict_action:
        action_price_euros.append((action, dict_action[action]['price'], dict_action[action]['euros']))

    all_combinations = []
    for L in range(0, len(action_price_euros) + 1):
        for subset in itertools.combinations(action_price_euros, L):
            all_combinations.append(subset)

    possible_combinations_with_constraints = []

    pbar = tqdm(all_combinations)
    pbar.set_description('- Search all combinations in progress -')
    pbar.unit = ' combinations'

    for combination in pbar:
        nb_items = len(combination)
        if nb_items >= 1:
            calcul_invest = 0
            calcul_benef = 0
            list_actions = []
            for i in range(0, nb_items):
                calcul_invest += round(combination[i][1], 2)
                calcul_benef += round(combination[i][2], 2)
                list_actions.append(combination[i][0])
            if MAX_VALUE_INVEST - calcul_invest >= 0:
                rendement = round(calcul_benef / calcul_invest * 100, 2)
                possible_combinations_with_constraints.append(
                    (list_actions, round(calcul_benef, 2), round(calcul_invest, 2), rendement)
                )

    return possible_combinations_with_constraints


def sort_by_invest_performance(x):
    """
    sort by invest and performance
    :param x:
    :return:a sorted list of actions
    """
    return [-x[2], -x[3]]


def sort_by_returns(x):
    """
    sort by returns (in percent)
    :param x:
    :return: a sorted list of actions
    """
    return [-x[3], -x[2]]


def sort_by_profit(x):
    """
    sort by profit (in euros)
    :param x:
    :return: a sorted list of actions
    """
    return [-x[1], -x[3]]


def brut_force_actions(csv_file):
    dict_action = recuperation_information(csv_file)
    calculate_profit_euros(dict_action)
    all_possibilities = search_all_possible_combinations(dict_action)
    print("\nYou have the opportunity to see the top 10 possible stock combinations :\n"
          "1 - biggest profit to smallest profit\n"
          "2 - largest to smallest returns\n"
          "3 - largest to smallest amount invested / returns \n")
    choice = False
    while not choice:
        response = input("Your choice : ")
        if response == '1':
            all_possibilities = sorted(all_possibilities, key=sort_by_profit)
        elif response == '2':
            all_possibilities = sorted(all_possibilities, key=sort_by_returns)
        elif response == '3':
            all_possibilities = sorted(all_possibilities, key=sort_by_invest_performance)
        if response == '1' or response == '2' or response == '3':

            print(f"List of stocks to invest in : {all_possibilities[0][0]}  \n"
                  f"Net profit over 2 years : {all_possibilities[0][1]}€ \n"
                  f"Initial investment : {all_possibilities[0][2]}€ \n"
                  f"Stock returns : {all_possibilities[0][3]}% \n"
                  f"----------------------------------------------------\n")

            stop_execution = input("Would you like to continue? (Y/n)")

        else:
            stop_execution = input("Your answer does not match any available choices. "
                                   "Would you like to continue? (Y/n)")

        if stop_execution.upper() == 'N':
            choice = True


if __name__ == '__main__':
    brut_force_actions('../csv/data_20_actions.csv')
