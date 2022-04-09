#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 19:29:12 2022

@author: rushikeshnaik
"""

def party(greeting):
    
    def guest(msg): #create a function as a nested function
        print(greeting+" "+msg) #use readonly state from outside
    
    return guest

def main():
    print("This is example of closure")
    p1 = party("halloween")
    p2 = party("new yar")
    p1("Rushi")
    p2("Luba")

if __name__ == "__main__":
    main()
    