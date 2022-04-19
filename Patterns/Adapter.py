#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 19:05:45 2022

@author: rushikeshnaik
"""

"""

THE CLIENT WANTS TO UE THE SPEAK() METHOD

WE HAVE SPEAK_ENGLISH and SPEAK_HINDI

ADAPTER Servers has the class that converts for the client

"""

class English:
    def __init__(self):
        self.name = "English"
        
    def speak_English(self):
        return "Hello"

class Hindi:
    def __init__(self):
        self.name = "Hindi"
    
    def speak_Hindi(self):
        return "Namaste"

class Adapter:
    def __init__(self,obj,**kwrs):
        #print("Adapter has been called")
        self._innerObject = obj
        self.__dict__.update(kwrs)        
    
    def __getattr__(self,attributeName):
        return getattr(self._innerObject,attributeName)
    
    def speak(self):
        pass

def main():
    
    greetings = []
    
    #greet in English
    
    greetings.append(Adapter(English(), speak=English().speak_English))
                    
    #greet in Hindi
    
    greetings.append(Adapter(Hindi(), speak=Hindi().speak_Hindi))
    
    for greet in greetings:
        print(greet.speak(),"in ",greet.name)

if __name__=="__main__":
    main()
    
    
    
    
    


        