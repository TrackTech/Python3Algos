#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 12:40:46 2021

@author: rushikeshnaik
"""
import requests
import json
import pandas as pd

parkActivities = []

class Park:
    def __init__(self,fullName,state):
        self.fullName = fullName
        self.state = state
        
class Activity:
    def __init__(self,actId,name,parks):
        self.actId = actId
        self.name = name
        if len(parks):
            self.parks = []
            for park in parks:
                for s in park["states"].split(","):
                    p = Park(park["fullName"],s)                
                    self.parks.append(p)
        
    
    def getParkListByState(self):
        output = {}
        for park in self.parks:
            if park.state in output:
                output[park.state].append(park.fullName)
            else:
                output[park.state] = [park.fullName]

class WWWCalls:
    
    apiKey = "oCj4j0K0zrDploMNElosU37CMwWlcLmQXDKCYJdS"
    baseURL = "developer.nps.gov/api/v1"
    
    def __init__(self):
        print("Hello WwwCalls has been initiated")
        
    @staticmethod
    def get(authentication,resource):
        if authentication == "basicHttp":
            raise NotImplementedError
            api = "https://"+WWWCalls.apiKey + "@" + WWWCalls.baseURL + resource
            print(api)
            response = requests.get(api)
            print(response)
        
        if authentication == "queryParameter":
            api = "https://"+WWWCalls.baseURL + resource
            params = {
                "api_key":WWWCalls.apiKey
                }
            response = requests.get(api,params)
            #print(type(response))
            print(response.headers)
            print(response.status_code)
            #print(response.json())
            
        if authentication=="headers":
            api = "https://"+WWWCalls.baseURL + resource
            headers = {"X-Api-Key":WWWCalls.apiKey}
            response = requests.get(api,headers=headers)
            
            with open("data.json","w") as dataFile:
                json.dump(response.json(),dataFile)
            
            
            
    
    def post(self):        
        print(self.apiKey)


def readData(fileName="data.json"):
    resp = None
    
    with open(fileName) as dataFile:
        resp = json.load(dataFile)
        
    for activity in resp["data"]:
        #print(activity)
        act = Activity(activity['id'],activity['name'],activity['parks'])
        parkActivities.append(act)
    

def getParkListByState():
    dic = {}
    
    for activity in parkActivities:
        for p in activity.parks:
            if p.state in dic:
                dic[p.state].add(p.fullName)
            else:
                dic[p.state] = set([p.fullName])
    
    return dic
   
def displayGraph():
    
        print("there are 2 errors, learning point")
        # data
        readData()
        
        dic = getParkListByState()
        
        dic2 = {}
        
        for k,v in dic.items():
            dic2[k]=len(v)
        
        print(dic2)
        #df = pd.DataFrame.from_dict(dic2,orient="index",columns=["State"])
        df = pd.DataFrame({'States':dic2.keys(),'NPS':dic2.values()})
                
        print("*******************************************")
        print("BELOW CODE DOES NOT WORK AS all column lenght shold be same")
        #df = pd.DataFrame().from_dict(dic)
        
        print("Below is working")
        #df.plot.bar(x='States',y='NPS',xlabel='States',ylabel='# of NPs').show()
        
        statesToShow = set(['AL','CA','CO','AR','AL','FL','NE'])
        dic3 = {}
        
        
        
        for k in sorted(statesToShow):
            print(k)
            if k in dic2:    
                dic3[k] = dic2[k]
        
        print(dic3)
    
        #dic3 = sorted(dic3.items().sort(i))
        df = pd.DataFrame({'States':dic3.keys(),'NPS':dic3.values()},index=statesToShow)
        df.plot.bar(x='States',y='NPS',xlabel='States',ylabel='# of NPs',rot=0)
        
        
        
        
        
        
        

def main():
    print("The request module will encode the parameters")
    try:
        print("Fetch data by one of **TWO** working ways")
        #WWWCalls.get("basicHttp","/activities/parks")
        #WWWCalls.get("queryParameter","/activities/parks")
        #WWWCalls.get("headers", "/activities/parks")
    except: 
        print("error occured")
    
    displayGraph()
    
    
    
    
if __name__ == "__main__":
    main()