#! /usr/bin/env python3
# coding: utf-8

from itertools import combinations


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


def sorted_by_percent(dict_actions):
    sorted_dict_actions = sorted(dict_actions.items(), key=lambda x: x[1]['benefice'], reverse=True)
    print(sorted_dict_actions)
    return sorted_dict_actions



if __name__ == '__main__':
    calcul_benefice_euros(dict_action)

    list_actions = sorted_by_percent(dict_action)


