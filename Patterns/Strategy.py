#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 19:48:34 2022

@author: rushikeshnaik
"""
import types

"""
THE STRATEGY IS USED AS THERE EXISTS A 'HAS-A' RELATION
POLYMORPHISM WOULD BE USED IF THERE WAS 'IS-A' RELATION
"""

class Strategy:
    
    def __init__(self,function=None):
        """This is the stratey class"""
        
        if function:
            self.execute = types.MethodType(function, self)
    
    def execute(self):
        print("I am the default method in",self.__class__.__name__)
    

def execute1(self):
    print("I am execute1 method in",self.__class__.__name__)

def main():
    s = Strategy()
    s.execute()
    
    s1 = Strategy(execute1)
    s1.execute()

if __name__=="__main__":
    main()
    
    