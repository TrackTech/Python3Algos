#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 22:45:15 2022

@author: rushikeshnaik
"""

from abc import abstractclassmethod,ABC

class Subject:
    
    def __init__(self):
        self._observers = []
        print("Subject initiated")
        
    
    def attach(self,observer):
        if not observer in self._observers:
            self._observers.append(observer)
    
    def detach(self,observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            print("observer does not exists")
        
    def notifyObservers(self):
        for obj in self._observers:
            obj.actOnInformation(self)
    
class Stock(Subject):
    def __init__(self,p):
        Subject.__init__(self)
        self._price = p
    
    @property
    def Price(self):
        return self._price
    
    @Price.setter
    def Price(self,p):
        self._price = p
        self.notifyObservers()

class Observer(ABC):
    
    @abstractclassmethod
    def actOnInformation(self,subject):
        pass

class PrintPrice(Observer):
    
    def actOnInformation(self, subject):
        print("The current price is",subject.Price)
        
class AlertPrice(Observer):
    
    def actOnInformation(self, subject):
        print("We should buy as stock price is",subject.Price)

def main():
    s = Stock(100)
    p1 = PrintPrice()
    a1 = AlertPrice()
    
    s.attach(p1)
    s.attach(a1)
    
    s.Price = 200
    
    s.Price = 300
    
if __name__=="__main__":
    main()
        
            