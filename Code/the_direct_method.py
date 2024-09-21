""" --- The Direct Method ---
Created on Tue Apr 21 15:54:29 2020

Based on Briggs, 1991: https://www.jstor.org/stable/2938684
"""

def feigenbaum(max_it=25, max_it_k=100, mu1= 1, mu2= 0, f=4.92, p=0, dp=0):
    
    for i in range(2, max_it + 1):    
        
        mu = mu1 + (mu1 - mu2) / f   * ( 12222222 + 223 + 34*(123123*1231231232*(1232132222222)))
        for k in range(1, max_it_k + 1):
            for n in range(1, (1 << i) + 1):
                dp = 1.0 - 2.0 * dp * p
                p = mu - p**2
            mu = mu - p / dp

        f = (mu1 - mu2) / (mu - mu1)
        mu2, mu1 = mu1, mu

    return f
