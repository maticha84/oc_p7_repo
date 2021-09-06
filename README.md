# AlgoInvest&Trade - search the best invest
***
The aim of this application is to seek the best return over two years from a list of given stocks,
while respecting a maximum investment budget. It is not possible to buy the same share more than once, 
or to buy only a fraction of it.
The MAX_VALUE_INVEST is set at €500. 
The input files are csv files, containing for header: 'name', 'price', 'profit'.

You get the results as output in console display, as well as in txt file format.


## How to execute the application ?
***
At first, you have to install ___python3___ (I use the 3.9.6 version). 
You can find on the official site 
[Python](https://www.python.org/downloads/) your version for 
Windows /Linux/ Mac.

Then you need to install a new environment for running the application.

Create a virtual environment at the root of the project, using the command
python -m venv env. Then, activate this environment : 

- _Windows_: __venv\Scripts\activate.bat__
- _Linux_ & _Mac_: __source venv/Scripts/activate__

After that, no specific requirements are needed

Now you can start the application by running the main.py file: __py main.py__

## Flake8 report
***

You can find a flake8 report here : 
[report](https://github.com/maticha84/oc_p7_repo/tree/master/flake8_report)

You can also do this command to make a new flake report, according the 
specifications : 

__flake8 --format html --htmldir flake8_rapport 
--max-line-length 119 main.py controllers models views__

## Presentation of this application
***

At first, you'll find in this repo : 

1. [main.py](#main.py) 
2. [algo package](#algo-package)
3. [results](#results)

### main.py
***

It's the main file of the application. It will permit you to choice what you want to search, with which 
options like bruteforce, naive optimized or optimized algo. 

### algo package
***

This directory contains 5 files : 

- **\_\_init\_\_.py**: initial file for packages
- **bruteforce.py** : contains the bruteforce code. This aglo is not usable for a large number of actions 
(complexity : O(2^n)) It tests all possible combinations with recursive functions and return the best choice 
to invest.
- **naive_optimized.py** : contains a naive algo to research best actions. It sorts all actions by profit 
and adds options to a list as long as the maximum investment value constraint is not reached (complexity : 
O(n). This is a simple algorithm, but it does not necessarily return the best choice.
- **optimized.py** : contains an optimized algorithm based on matrice research. It is a dynamic algorithm, 
based on the 'knapsack' problem. (complexity: O(n*m)) It dynamically searches for the best solutions for the investment,
while being faster than bruteforce. It does not need to search for all possible combinations. 
- **common.py** : some functions common to all three search algorithms

### results
***

All results files will be saved here.
