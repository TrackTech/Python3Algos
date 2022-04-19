#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 19:58:26 2022

@author: rushikeshnaik
"""

import copy

class Car:
    def __init__(self):
        self.name = "Mustang"
        self.color = "Red"
        self.price = 1000
        
    def __str__(self):
         
        return "{} | {} | {}".format(self.name,self.color,self.price)
    

class Prototype:
    def __init__(self):
        self.objs = {}
        
    def register_object(self,name,obj):
        self.objs[name] = obj
        
    def clone(self,name,**kwargs):
       
        obj = copy.deepcopy(self.objs.get(name))
        
        obj.__dict__.update(kwargs)
        
        return obj

def main():
    print("PROTOTYPE SOLVES the PROBLEM of CLONING AN OBJECT AS CLOSNING IS FATER THAN CREATING A NEW OBJECT")
    
    c = Car()
    
    prototype = Prototype()
    
    prototype.register_object("car", c)
    
    c1 = prototype.clone("car")
    
    print(c1)
    
    c2 = prototype.clone("car",color="Green") 
    
    print("**kwargs is used by passing property name and value. color='Green'. No double quotes for color")
    
    print(c2)

if __name__=="__main__":
    main()