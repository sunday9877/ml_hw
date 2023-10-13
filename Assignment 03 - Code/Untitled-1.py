"""
If  and  is a positive real number, the iteration

converges to the square root of . Write a Python function that runs this iteration until the difference between  and  is less than a tolerance.

def sq(n):
    x=1
    tol = 1
    while(tol>1e-6):
        xnew = # fill this in
        tol = np.abs(xnew - x)
        x = xnew
    return x

Now improve the function above so that:

one can optionally provide a threshold to replace 1e-6
if the code runs for more than max_iter iterations of the while loop, it quits while printing “Failed to converge”. max_iter is by default 1000 but can be modified when the function is called.
"""
import numpy as np

def sq(n, tol=1e-6, max_iter=1000):
    x=1
    i=0
    while(i<max_iter):
        xnew = 0.5*(x+n/x)
        if np.abs(xnew - x) < tol:
            return xnew
        x = xnew
        i += 1
    print("Failed to converge")
    return xnew