#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 20:16:03 2022

@author: rushikeshnaik
"""

from abc import ABC

class Singleton:
    
    singletonDict = {}
    
    
    

class MyInstance(Singleton):
    
    def __init__(self):
        self.myDict = Singleton.singletonDict
        
    
    def addKV(self,key,value):
        self.myDict[key] = value
        
    def printMe(self):
        print(self.myDict)
    
def main():
    
    i1 = MyInstance()
    
    i1.addKV("hello", "world")
    
    i2 = MyInstance()
    
    i2.addKV("star", "track")
    
    i1.printMe()
    
    i2.printMe()
    
    print("here both object yield same dictionary values")
    
if __name__ == "__main__":
    main()
    

