#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:54:13 2022

@author: rushikeshnaik
"""

from abc import ABC, abstractmethod

class AbstractVisitor(ABC):
    
    @abstractmethod
    def visit(self,house):
        pass
    
class Electrician(AbstractVisitor):
    
    def __init__(self,n):
        self.name = n
    
    def visit(self,house):
        house.workWithElectrician(self)
        

class Plumber(AbstractVisitor):
    
    def __init__(self,n):
        self.name = n
    
    def visit(self,house):
        house.workWithPlumber(self)

class House:
    
    def __init__(self,n):
        self.electrical = "Wires"
        self.plumbing = "Tubes"
        self.name = n
    
    def acceptVistor(self,visitor):
        visitor.visit(self)
        
        print("INSTEAD OF WRITING MULTIPLE IF STATEMENTS")
        """
        if isinstance(visitor, Electrician):
            self.workWithElectrician(visitor)
        if isinstance(visitor, Plumber):
            self.workWithPlumber(visitor)
        """
    
    def workWithElectrician(self,electrician):
        print(electrician.name,"-Electrician visited",self.name,"and worked on",self.electrical)
        
    def workWithPlumber(self,plumber):
        print(plumber.name,"-Plumber visited",self.name,"and worked on",self.plumbing)

def main():
    h = House("Kayellen")
    e = Electrician("Rushikesh")
    h.acceptVistor(e)

if __name__=="__main__":
    main()