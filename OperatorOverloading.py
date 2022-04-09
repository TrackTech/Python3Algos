#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 22:41:43 2022

@author: rushikeshnaik
"""


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __eq__(self,p):
        return self.x==p.x and self.y==p.y

def main():
    p1 = Point(1,2)
    p2 = Point(1,2)
    p3 = Point(2,3)
    print("Operator Overloading")
    print(p1==p2)
    print(p2==p3)
    
if __name__=="__main__":
    main()