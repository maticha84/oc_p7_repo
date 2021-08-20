#! /usr/bin/env python3
# coding: utf-8

import itertools

max_value_invest = 500
dict_action = {
    'action_1': {'cout': 20, 'benefice': 0.05},
    'action_2': {'cout': 50, 'benefice': 0.10},
    'action_3': {'cout': 50, 'benefice': 0.15},
    'action_4': {'cout': 70, 'benefice': 0.20},
    'action_5': {'cout': 60, 'benefice': 0.17},
    'action_6': {'cout': 80, 'benefice': 0.25},
    'action_7': {'cout': 22, 'benefice': 0.07},
    'action_8': {'cout': 26, 'benefice': 0.11},
    'action_9': {'cout': 48, 'benefice': 0.13},
    'action_10': {'cout': 34, 'benefice': 0.27},
    'action_11': {'cout': 42, 'benefice': 0.17},
    'action_12': {'cout': 110, 'benefice': 0.09},
    'action_13': {'cout': 38, 'benefice': 0.23},
    'action_14': {'cout': 14, 'benefice': 0.01},
    'action_15': {'cout': 18, 'benefice': 0.03},
    'action_16': {'cout': 8, 'benefice': 0.08},
    'action_17': {'cout': 4, 'benefice': 0.12},
    'action_18': {'cout': 10, 'benefice': 0.14},
    'action_19': {'cout': 24, 'benefice': 0.21},
    'action_20': {'cout': 114, 'benefice': 0.18}
}


def calcul_benefice_euros(dict_action):
    for action in dict_action:
        dict_action[action]['euros'] = round(dict_action[action]['cout'] * dict_action[action]['benefice'], 2)


def search_all_possible_combinations(dict_action, max_value_invest=500):
    action_cout_euros = []
    for action in dict_action:
        action_cout_euros.append((action, dict_action[action]['cout'], dict_action[action]['euros']))

    all_combinations = []
    for L in range(0, len(action_cout_euros) + 1):
        for subset in itertools.combinations(action_cout_euros, L):
            all_combinations.append(subset)

    possible_combinations_with_constraints = []
    none_possible = []
    for combination in all_combinations:
        nb_items = len(combination)
        if nb_items >= 1:
            calcul_invest = 0
            calcul_benef = 0
            list_actions = []
            for i in range(0, nb_items):
                calcul_invest += round(combination[i][1], 2)
                calcul_benef += round(combination[i][2], 2)
                list_actions.append(combination[i][0])
            if max_value_invest - calcul_invest >= 0:
                rendement = round(calcul_benef / calcul_invest * 100, 2)
                possible_combinations_with_constraints.append(
                    (list_actions, round(calcul_benef, 2), round(calcul_invest, 2), rendement)
                )
            else:
                none_possible.append(list_actions)
    return possible_combinations_with_constraints


def tri_par_invest_rendement(x):
    return [-x[2], -x[3]]


def tri_par_rendement_invest(x):
    return [-x[3], -x[2]]


def tri_benefice_rendement(x):
    return [-x[1], -x[3]]


if __name__ == '__main__':
    calcul_benefice_euros(dict_action)
    all_possibilities = search_all_possible_combinations(dict_action)
    print("Vous avez la possibilité de voir les 10 meilleures combinaisons d'actions possibles :\n"
          "1 - du plus gros bénéfice au plus petit bénéfice\n"
          "2 - du plus gros au plus petit rendement\n"
          "3 - de la plus grosse à la plus petite somme investie\n")
    choix = False
    while not choix:
        response = input("Votre choix : ")
        if response == '1':
            all_possibilities = sorted(all_possibilities, key=tri_benefice_rendement)
        elif response == '2':
            all_possibilities = sorted(all_possibilities, key=tri_par_rendement_invest)
        elif response == '3':
            all_possibilities = sorted(all_possibilities, key=tri_par_invest_rendement)
        if response == '1' or response == '2' or response == '3':
            for i in range(0, 10):
                print(f"liste des actions où investir : {all_possibilities[i][0]}  \n"
                      f"Bénéfice net sur 2 ans : {all_possibilities[i][1]}€ \n"
                      f"Investissement de départ : {all_possibilities[i][2]}€ \n"
                      f"Rendement des actions : {all_possibilities[i][3]}% \n"
                      f"----------------------------------------------------\n")

            stop_execution = input("On continue ? (O/n)")
            if stop_execution.upper() == 'N':
                choix = True
