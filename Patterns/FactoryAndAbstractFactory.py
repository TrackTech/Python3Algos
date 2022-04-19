#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 22:41:45 2022

@author: rushikeshnaik
"""


class Dog:
    def getType(self):
        print("I am dog")

class DogFood:
    def getType(self):
        print("I am dogfood")
    
class Cat:
    def getType(self):
        print("I am cat")
    
class CatFood:
    def getType(self):
        print("I am catfood")
    
def PetFactory(name):
    
    pets = {
        "Cat":Cat,
        "Dog":Dog
        }
    
    return pets[name]()

class DogFactory:
    
    def getPet(self):
        return Dog()
    
    def getFood(self):
        return DogFood()

class CatFactory:
    
    def getPet(self):
        return Cat()
    
    def getFood(self):
        return CatFood()

def PetAbstractFactory(name):
    
    petFactory = {
        "Dog":DogFactory,
        "Cat":CatFactory
        }
    
    return petFactory[name]()
    

def main():
    
    print("Factory method takes input and returns an object of a particular type")
    
    obj = PetFactory("Dog")

    obj.getType()
    
    
    print("Abstract factory return a factory based on input. The factory itself groups related objects.")
    
    abstractFactor = PetAbstractFactory("Dog")
    
    pet = abstractFactor.getPet()
    
    
    pet.getType()



if __name__=="__main__":
    main()        
    
    
    