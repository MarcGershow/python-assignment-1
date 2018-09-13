#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem Set 1, part C
    builds on parts A,B to calculate how much
    I need to stock a way to save ONE MILLION DOLLARS
    
    PS, I now feel old, because the Austin Powers ONE MILLION DOLLARS
    joke is older than any of you are

    @author: Your name
    TA: Your TAs Name
    Assignment: PS1 partA
       

"""

MAX_CONTRIBUTION = 18500.0
BASE_FRACTION = 0.05
MATCH_FRACTION = 0.05


DEFAULT_RATE_OF_RETURN = 3.0
DEFAULT_RAISE = 0.0
DEFAULT_GOAL = 1000000
DEFAULT_PRECISION = 0.1

MAX_YEARS_BEFORE_RETIREMENT = 40

import numpy as np

#copy any code you need over from partA

def partCMain():
    """write a descriptive docstring!
    """
    print("This function should ask for salary and number of years to work, then tell me how much I need to save to retire with")
    print("ONE MILLION DOLLARS")
    print("or whatever we have put in for DEFAULT_GOAL, because we don't hard code numbers in this class")
    
def calculateSavingsRate(salary, numyears, goal = DEFAULT_GOAL, 
                         rateOfReturn = DEFAULT_RATE_OF_RETURN, annualRaise = DEFAULT_RAISE, 
                         precision = DEFAULT_PRECISION):
    """ finds the percentage you should contribute to your retirement plan to meet your goal

    parameters
    ----------
    salary : float
        staring salary year 1
    numyears : int
        how many years you plan to work         
    goal : float, optional
        how much you want to have in the bank at retirement, (default $1M)
    rateOfReturn : float, optional
        annual interest rate (adjusted for inflation) for savings (default 3%)
    annualRaise : float, optional
        annual amount of raise (adjusted for inflation) (default 3%)
    precision : float, optional
        how precisely to calculate the savings rate (default 0.1%)
    
    returns
    -------
    float
        savings rate. -1 indicates 0% is sufficient to meet goal. Inf indicates 100% is insufficient
    """
    return 0.0 #it better do more than this when you're done with it!

    #use bisectional search strategy, described in your book on p. 30
 
#you will need to write at least one more function to figure out how many years you'll need to work while making
#the maximum contribution to retire with 1,000,000

#don't edit the lines below;
#they will run partCMain if you execute the module as a script, but not if it's loaded
#from another module -- don't worry about understanding this yet
if __name__== "__main__":
    partCMain()