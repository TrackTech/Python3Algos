#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 17:33:51 2021

@author: rushikeshnaik
"""
import pandas as pd
import matplotlib.pyplot as plt

def main():
    dtmap = {
        "PassengerId":int
    }
    df = pd.read_csv("./train.csv",dtype=dtmap)

    dfChildren = df[df['Age']<20]

    print(df.shape)
    print(dfChildren.columns)
    print(dfChildren.head)
    # print(dfChildren['PassengerId','Age'])
    print(dfChildren[['PassengerId', 'Age']])

    # dfNull = df[df["PassengerId"].isnull()]

    # dfNonNull = df.dropna(subset=['PassengerId'])

    # print(dfNonNull)

    # print(df["PassengerId"].map(type))

    # passengers = df.to_records(index=False)
    # cnt =0
    # for person in passengers:
    #     cnt+=1
    #     if cnt==10:
    #         break
    #     print(type(person),person.Name)
    
    

    # for person in passengers:
    #     cnt+=1
    #     if cnt==10:
    #         break
    #     print(person)



 
if __name__ == "__main__":
    main()
