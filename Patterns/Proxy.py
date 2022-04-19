#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 08:06:11 2022

@author: rushikeshnaik
"""

import time

"""

DELAY THE CREATION OF RESOURCE INTENSIVE OBJECT TILL ALL PREPROCESSING IS COMPLETE

"""

class Barcode:
    def __init__(self):
        print("Lock the dbs")
        print("this is highly resource oriented")

class Proxy:
    
    def __init__(self):
        self.preprocessingDone = False
        self.barcode = None
    
    def produce(self):
        if self.preprocessingDone:
            self.barcode = Barcode()
            return True
        
        else:
            time.sleep(2)
            print("Sleeps for 2 seconds")
            return False
        

def main():
    
    p = Proxy()
    
    p.produce()
    
    p.preprocessingDone = True
    
    p.produce()
    
if __name__ == "__main__":
    main()
        
        