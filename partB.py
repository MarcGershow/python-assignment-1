#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem Set 1, part B
    builds on partA to calculate the total savings at retirement

    @author: Your name
    TA: Your TAs Name
    Assignment: PS1 partA
       

"""

MAX_CONTRIBUTION = 18500.0
BASE_FRACTION = 0.05
MATCH_FRACTION = 0.05


import numpy as np

#copy any code you need over from partA

def partBMain():
    """write a descriptive docstring!
    """
    print("This function should ask for salary, contribution PERCENTAGE of salary, rate of return on investment,  annual raise, and number of years to work")
    print("Then it should tell me how much money I will have saved for retirement")
    print("Cool tricks -- round(1.2345,2) = ", round(1.2345,2), " and sep='' as an optional argument gets rid of spaces, so you can print $", 1000.00, sep='')
    
 
def calculateRetirementSavings(salary, savingsPercent, rateOfReturn, annualRaise, numyears):
    """calculates how much money you'll have saved at retirement
    
    parameters
    ----------
    salary : float
        staring salary year 1
    savingsPercent : float
        the percentage of salary to save every year
    rateOfReturn : float
        annual interest rate (adjusted for inflation) for savings
    annualRaise : float
        annual amount of raise (adjusted for inflation)
    numyears : int
        how many years you plan to work
            
    returns
    -------
    float
        amount of money saved at retirement
    """
    return 0.0 #no soup for you! replace with your own code

#don't edit the lines below;
#they will run partBMain if you execute the module as a script, but not if it's loaded
#from another module -- don't worry about understanding this yet
if __name__== "__main__":
    partBMain()