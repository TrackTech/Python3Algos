#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 21:02:36 2022

@author: rushikeshnaik
"""

from abc import ABC,abstractclassmethod

class Car:
    def __init__(self):
        self.price = 0
        self.color = None
        self.name = None
        
class Builder():
    
    def __init__(self):
        self.car = Car()
    
    #@abstractclassmethod
    def setColor(self):
        pass
    
    #@abstractclassmethod
    def setPrice(self):
        pass
    
    def getCar(self):
        print(self.car.name,self.car.price,self.car.color)
    
    

class ToyotaBuilder(Builder):
    def __init__(self):
        #
        super().__init__()
        self.car.name = "Toyota"
        
    def setPrice(self):
        self.car.price = 1000
    
    def setColor(self):
        self.car.color = "Blue"
    
class HondaBuilder(Builder):
    def __init__(self):
        super().__init__()        
        self.car.name = "Honda"
    
    
    def setPrice(self):
        self.car.price = 1500
    
    def setColor(self):
        self.car.color = "Red"

class Director():
    def __init__(self,builder):
        self.builder = builder
    
    def createCar(self):
        self.builder.setPrice()
        self.builder.setColor()
    
    def getCar(self):
        self.builder.getCar()
        
    
def main():
  
    builder = ToyotaBuilder()
    
    director = Director(builder)
    
    director.createCar()
    
    director.getCar()
   
    
if __name__=="__main__":
    main()

    