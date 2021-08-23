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
        for row in reader:
            if float(row['price']) > 0 and float(row['profit']) > 0:
                dict_action[row['name']] = {
                    'price': float(row['price']),
                    'profit': float(row['profit']),
                    'euros': round(float(row['price']) * float(row['profit']) / 100, 2)
                }
    dict_action = sorted(dict_action.items(), key=lambda x: x[1]['profit'], reverse=True)
    return dict_action


if __name__ == '__main__':
    dict_actions = recuperation_information('dataset2.csv')
    print(dict_actions)
    print(len(dict_actions))
