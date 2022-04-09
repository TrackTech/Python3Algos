#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 20:38:48 2022

@author: rushikeshnaik
"""



def myDecoratorList(func):
    
    def inner(*args):
        name = func.__name__ + "|"
        
        newArgs = map(str,args)
        
        name+="|".join(list(newArgs))
        
        print(name)
        
        func(*args)
    
    return inner

def myDecoratorDict(func):
    
    
    def inner(**kwargs):
        
        name = func.__name__
        
        for k,v in kwargs.items():
            name+="|"+k+"_"+str(v)
        
        print(name)
        
        func(**kwargs)
    return inner
    
@myDecoratorList
def testMe():
    print("Test Me called")

@myDecoratorList
def testMe2(a,b):
    print("Test me 2 called")

@myDecoratorDict    
def testMe3(a,b):
    print(a-b)  
    
def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner
 
def decor(func):
    def inner():
        x = func()
        return x/2
    return inner
 
@decor1  #second to execute
@decor   #First to execute
def num():
    return 10
    
def main():
    testMe()
    testMe2(5,10)
    testMe3(b=5,a=100)
    n = num()
    print(n)
    
if __name__ == "__main__":
    main()
    
    
    
 