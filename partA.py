#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem Set 1, part A
functions to coerce a salary contribution into the correct range
    and to calculate the NYU salary match
    and code to interactively demonstrate how these functions work

    @author: Your name
    TA: Your TAs Name
    Assignment: PS1 partA
       

"""

MAX_CONTRIBUTION = 18500.0
BASE_FRACTION = 0.05
MATCH_FRACTION = 0.05

import numpy as np

def partAMain():
    """prompts the user for salary and contribution dollar amounts,
       then displays a message breaking down the actual contributions
       
       example output (user input in {}):
           please enter your salary > {25000}
           please enter amount to contribute > {5000}
           You will contribute 5000.0 and nyu will contribute 2500.0 for a total of 7500.0
           
           please enter your salary > {250000}
           please enter amount to contribute > {50000}
           You will contribute 18500.0 and nyu will contribute 25000.0 for a total of 43500.0
           
           please enter your salary > {30000}
           please enter amount to contribute > {0}
           You will contribute 0.0 and nyu will contribute 1500.0 for a total of 1500.0           
    """
    print ("This function does not do anything useful") #placeholder - delete and replace with your own code
    print ("but it will, once you write some awesome code") #placeholder - delete and replace with your own code
    #I wrote a helper function, getNumberInput that may be useful to you in this function

def coerceContribution(salary, contribution):
    """coerces the retirement plan contribution into the nearest legal value
    
    parameters
    ----------
    salary: float
        the total annual salary
    contribution: float
        the desired contribution amount 
        
    returns
    --------
        float
            coerced contribution, which is in the range of [0, min(salary, MAX_CONTRIBUTION)]
    """
    return 0.0 #placeholder - delete and replace with your own code


def calculateTotalContribution(salary, contribution):
    """finds the total amount contributed to the retirement plan
    
    parameters
    ----------
    salary: float
        the total annual salary
    contribution: float
        the desired contribution amount 
        
    returns
    --------
    (total_contribution, nyu_portion) : float
        the total amount contributed to the retirement plan and nyu's portion of that contribution
    
    NYU contributes BASE_FRACTION of salary plus the lesser of MATCH_FRACTION*salary and contribution
    """
    return (0.0, 0.0) #placeholder - delete and replace with your own code
    


def getNumberInput (prompt, validRange = [-np.Inf, np.Inf]):
    """displays prompt and converts user input to a number
    
       in case of non-numeric input, re-prompts user for numeric input
       
       Parameters
       ----------
           prompt : str
               prompt displayed to user
           validRange : list, optional
               two element list of form [min, max]
               value entered must be in range [min, max] inclusive
        Returns
        -------
            float
                number entered by user
    """
    while True:
        try:
            num = float(input(prompt))
        except Exception:
            print ("Please enter a number")
        else:
            if (num >= validRange[0] and num <= validRange[1]):
                return num
            else:
                print ("Please enter a value in the range [", validRange[0], ",", validRange[1], ")") #Python 3 sytanx
            
    return num

#don't edit the lines below;
#they will run partAMain if you execute the module as a script, but not if it's loaded
#from another module -- don't worry about understanding this yet
if __name__== "__main__":
    partAMain()
    