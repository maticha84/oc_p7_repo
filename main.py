#! /usr/bin/env python3
# coding: utf-8
"""
Tis is the main menu to test all algorithm to search the best return
"""
from naive_optimized import run_naive_optimized
from optimized import run_optimized
from bruteforce import run_bruteforce
from os import path

print("\nWelcome to our algoInvest program.\n")

exit_application = False

while not exit_application:
    print(" Choose an option to continue : \n\n"
          "1- Bruteforce option (just for 20 actions)\n"
          "2- Naive optimized option \n"
          "3- Optimized option \n")
    choice = 0
    choice2 = 0
    choice_ok = False

    while not choice_ok:
        try:
            choice = int(input("Your choice : "))
            if choice == 1 or choice == 2 or choice == 3:
                choice_ok = True
        except ValueError:
            print("Your choice must be 1, 2 or 3")

    if choice == 1:
        run_bruteforce('data_20_actions.csv')

    elif choice == 2 or choice == 3:
        print("Which file do you want to test ?\n"
              "1- data_20_actions.csv\n"
              "2- dataset1.csv\n"
              "3- dataset2.csv\n"
              "4- another file\n")
        choice_ok = False
        while not choice_ok:
            try:
                choice2 = int(input("Your choice : "))
                if choice2 == 1 or choice2 == 2 or choice2 == 3 or choice2 == 4:
                    choice_ok = True
            except ValueError:
                print("Your choice must be 1, 2, 3 or 4")

        if choice2 == 1:
            csv_file = 'data_20_actions.csv'
        if choice2 == 2:
            csv_file = 'dataset1.csv'
        if choice2 == 3:
            csv_file = 'dataset2.csv'
        if choice2 == 4:
            csv_file_test = False
            while not csv_file_test:
                csv_file = input("Enter the name of csv file (file.csv) : ")
                csv_file_test = path.isfile(csv_file)

    if choice == 2:
        run_naive_optimized(csv_file)
    if choice == 3:
        run_optimized(csv_file)

    response = input("Do you want to exit the application ? (Y/n) : ")

    if response.upper() == 'Y':
        exit_application = True
