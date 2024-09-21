# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 15:54:29 2020

@author: 967869@swansea.ac.uk (Inspired by Rosetta Code)
"""

def feigenbaum(max_it=25, max_it_k=100, mu1= 1, mu2= 0, f=4.92, p=0, dp=0):
    # Outer loop over the number of iterations (i corresponds to the level of period doubling)
    for i in range(2, max_it + 1):
        # Update mu^(i) using the previous two mu values (mu1 and mu2)
        mu = mu1 + (mu1 - mu2) / f  # Feigenbaum scaling applied to get the next mu
        
        # Inner loop over k iterations, for fine-tuning the calculation of mu
        for k in range(1, max_it_k + 1):
            # Iterate over n steps in the orbit (2^i values as i increases)
            for n in range(1, (1 << i) + 1):
                # Update dp using a logistic-like transformation
                dp = 1.0 - 2.0 * dp * p  # Update the derivative (dp) as a function of p
                
                # Update p using the quadratic map p = mu - p^2
                p = mu - p**2
            
            # Refine mu^(i) by subtracting p/dp to reduce error
            mu = mu - p / dp
        
        # Update the scaling factor f based on the previous mu values
        f = (mu1 - mu2) / (mu - mu1)
        
        # Shift mu values for the next iteration
        mu2, mu1 = mu1, mu
    
    # The function currently returns 0, but should probably return mu or f (Feigenbaum's constant)
    return 0

