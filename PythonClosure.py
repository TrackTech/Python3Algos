#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 19:29:12 2022

@author: rushikeshnaik
"""

def party(party_name):
    
    def guest(name): #create a function as a nested function
        print(party_name+" "+name) #use readonly state from outside
    
    return guest

def main():
    print("This is example of closure")
    guest1 = party("halloween")
    guest2 = party("new yar")
    guest1("Rushi")
    guest2("Luba")

if __name__ == "__main__":
    main()
    