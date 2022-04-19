#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 21:10:43 2022

@author: rushikeshnaik
"""

from functools import wraps

def a_decorator(func):
    
    def wrapper(*args):
        """I am the wrapper function"""
        print(args)
        return func(*args)
    
    return wrapper

def b_decorator(func):
    
    @wraps(func)
    def wrapper(*args):
        """I am the wrapper function"""
        print(args)
        return func(*args)
    
    return wrapper


@a_decorator
def mySum(a,b):
    """I am mySum function """
    return a+b

@b_decorator
def mySum2(a,b):
    """I am mySum2 function """
    return a+b
    

def main():
    print(mySum(10,5))
    
    print(mySum.__name__) #This prints wrapper
    
    print(mySum.__doc__) #This print "I am the wrapper function 
    
    print(mySum2(10,5))
    
    print(mySum2.__name__) #This prints mySum2
    
    print(mySum2.__doc__) #This print "I am the mySum2 function 
    
    
    
if __name__ == "__main__":
    main()