#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 21:01:54 2022

@author: rushikeshnaik
"""

"""

    THIS PATTERN CREATES A HIERARCHY OF TREE
    HERE A COMPONENT CAN HAVE A CHILD OR ANOTHER COMPONENT
"""
class Component:
    
    def __init__(self):
        pass
    
    def component_function(self):
        pass

class Child(Component):
    def __init__(self,*args):
        self.name = args[0]
    
    def component_function(self):
        print("I am ",self.name," and I am a child")

class Composite(Component):
    def __init__(self,*args):
        self.name = args[0]
        self.children = []
        
    def addChild(self,child):
        self.children.append(child)        
    
    def removeChild(self,child):
        self.children.remove(child)
        
    def component_function(self):
        
        print("I am",self.name,"and I am a child")
        
        for c in self.children:
            c.component_function()

def main():
    
    luba = Child("Lubava")
    
    rushikesh = Composite("Rushikesh")
    rushikesh.addChild(luba)
    
    jayant = Composite("Jayant")
    jayant.addChild(rushikesh)

    jayant.component_function()
    
if __name__=="__main__":
    main()
        