#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 17:33:51 2021

@author: rushikeshnaik
"""
import pandas as pd

def main():
    
    print("Load a csv file")
    titanic_df = pd.read_csv("train.csv")
    
    print("Return first 10 rows")
    print(titanic_df.head(10))
    print("------------------------------------------------------------------")
    print("Return last 10 rows")
    print(titanic_df.tail(10))
    print("------------------------------------------------------------------")
    print("Return first 10 passenger ids")
    print(titanic_df.head(10)["PassengerId"])
    print("------------------------------------------------------------------")
    print("use describe method to provide basic summary excluding NAN values")
    print(titanic_df.describe())
    print("------------------------------------------------------------------")
    print("Size returns the number of rows and columns")
    print(titanic_df.size)
    print("------------------------------------------------------------------")
    print("Index states the types of index on the data, RangeIndex, datetime index")    
    print(titanic_df.index)
    print("List passenger by descending order of Fare")
    print(titanic_df.sort_values(by=['Fare'],ascending=False))
    
    print("Plot")    
    
    print(titanic_df["Fare"].round().value_counts().plot.bar(xlabel="Fare",ylabel="How many"))
    
    #print(titanic_df["Fare"].round().value_counts())
    
    data = titanic_df["Fare"].round()
    #print(data.where(data>500))
    #print(data.where(data>500).dropna())
    
    print("dropna method removes all NaN values")
    binData = pd.cut(data.where(data<10).dropna(),10)
    print("Bin data")
    #print(binData.value_counts())
    
    #print(binData.value_counts().plot(xlabel="count",ylabel="Fare Range"))
    
    print(binData.value_counts().plot.bar(xlabel="Count",ylabel="Fare Range"))
    
    print("Here closed='both' make sure both values are included i.e For (1,2) both 1 and 2 is included ")
    bins = pd.IntervalIndex.from_tuples([(0, 1), (2, 3), (4, 5),(6,7),(8,9),(10,11)],closed='both')
    
    
    binData = pd.cut(data.where(data<=10).dropna(),bins)
    
    #print("Total count:",data.where(data<=10).dropna().count())
    
    #print(data.where(data<=10).dropna().head(20))
    
    
    #print(binData.head(20))
    #print(binData.value_counts().plot.bar(xlabel="Count",ylabel="Fare Range"))
    
    print("rot=0 changes the way x axis shows the data labels")
    
    groupedBinData = binData.value_counts()
    print("By default the bars are plott by decreasing values of vals")
    print("sort_index() helps to sort by index i.e the way they are entered")
    sortedGroupedBinData = groupedBinData.sort_index()
    #print(type(groupedBinData))
    sortedGroupedBinData.plot.bar(xlabel="Count",ylabel="Fare Range",rot=0).show()
    
    
    
    
    
if __name__ == "__main__":
    main()