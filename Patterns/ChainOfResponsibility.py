#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 20:27:40 2022

@author: rushikeshnaik
"""

from abc import ABC,abstractmethod

class Handler(ABC):
    
    def __init__(self,successor):
        """Provide the next handler here"""
        self.successor = successor
    
    def process(self,request):
        if not self._execute(request):
            self.successor.process(request)
        else:
            return True
            
    @abstractmethod
    def _execute(self,request):
        pass

class IntHandler(Handler):
    
    def __init__(self,successor):
        """This is INT handler, Provide the next handler here"""
        super().__init__(successor)
    
    def _execute(self,request):
        if isinstance(request,int):
            print("This is int I will handle it.-",self.__class__.__name__)
            return True
        return False

class StringHandler(Handler):
    
    def __init__(self,successor):
        super().__init__(successor)
    
    def _execute(self,request):
        if isinstance(request,str):
            print("This is string I will handle it.-",self.__class__.__name__)
            return True
        return False

class DefaultHandler(Handler):
    
    def __init__(self,successor):
        super().__init__(successor)
    
    def _execute(self,request):        
        print("No one could handle it, so I will do so-",self.__class__.__name__)
        return True
        


def main():
    requests = ["abc",10,0.1]
    
    #handle = IntHandler(StringHandler(None))
    
    handle = IntHandler(StringHandler(DefaultHandler(None)))
    
    for req in requests:
        handle.process(req)
        
if __name__=="__main__":
    main()
        
    