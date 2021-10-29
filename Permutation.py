# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def printAllPermutations(lst):
    res = []
    def dfs(lst,state,path,target):
        
        #if state meets target output result
        if len(state)==target:
            res.append(path[:])
        
        for i in range(len(lst)):
            #make sure i is not in state
            if not i in state:
                state.add(i)
                path.append(lst[i])
                dfs(lst,state,path,target)
                state.remove(i)
                path.pop()
    
    dfs(lst,set([]),[],len(lst))
    print("---------------")
    print(res)


def printAllPermutationsNODups(lst):
    res = []
    recurNumber= -1
    
    def dfs(lst,state,path,target):
        nonlocal recurNumber
        recurNumber+=1
        #print("Recurrance:",recurNumber,", State:",state,", path:",path)
        if len(state)==target:
            res.append(path[:])
            #print("Result-Recurrance:",recurNumber,", State:",state,", path:",path)
            return
        
        for i in range(len(lst)):
            if not i in state:
                if i>0 and lst[i]==lst[i-1] and i-1 in state:
                    #print("declined entry:",i)
                    continue
                state.add(i)
                path.append(lst[i])
                dfs(lst,state,path,target)
                state.remove(i)
                path.pop()
                #print("Pop-Recurrance:",recurNumber,", State:",state,", path:",path)
    
    lst.sort()
    dfs(lst,set([]),[],len(lst))
    print("---------------")
    print(res)
    
def printAllPermutationsNODupsWithMap(lst):
    res = []
    hashMap={}
    for v in lst:
        if v in hashMap:
            hashMap[v]+=1
        else:
            hashMap[v]=1
            
    def dfs(dic,state,target):
         if len(state)==target:
             res.append(state[:])
             return
         keys = dic.keys()
         for key in keys:
             if dic[key]>0:
                 state.append(dic[key])
                 dic[key]-=1
                 dfs(dic,state,target)
                 dic[key]+=1
                 state.pop()    
                 
    dfs(hashMap,[],len(lst))
    print("---------------")
    print(res)

def getAllPermutations(lst):
    res = []
    
    def dfs(lst,state,path,target):
        #here there is no target size or value
        
        res.append(path[:])
        
        for i in range(len(lst)):
            if not i in state:
                state.add(i)
                path.append(lst[i])
                dfs(lst,state,path,target)
                state.remove(i)
                path.pop()
        
    dfs(lst,set([]),[],None)
    print("---------------")
    print(res)
            
def getAllUniqueCombinationsOfSizeLen(lst,combSize):
    res = []
    
    #combination does not allow duplicate values
    def dfs(lst,currIndex,path,target):
        if len(path)==target:
            res.append(list(path))
            return
        
        for i in range(currIndex,len(lst)): #by passing currIndex as state, you make sure it is not picked up            
            if not lst[i] in path: #by make sure Path is a set you do not let duplicate entries
                l = lst[i]
                path.add(l)
                dfs(lst,i+1,path,target)
                path.remove(l)
                    
    dfs(lst,0,set([]),combSize)
    print("---------------")
    print(res)
    

def getDifferentWaystoAchieveATotal(lst,total):
    #give a list, you can use the number in the list any number of times
    
    res = []
    
    def dfs(lst,state,path,target):
        
        if state==target:
            res.append(path[:])
            return       
        
        for i in lst:
            if state+i > state and state+i<=target:
            #if state+i<=target:
                path.append(i)
                state+=i
                dfs(lst,state,path,target)
                state-=i
                path.pop()
        
    dfs(set(lst),0,[],total)
    print("---------------")
    print(res)

def getDifferentWaystoAchieveATotalNoDups(lst,total):
    #give a list, you can use the number in the list any number of times
    lst = list(set(lst)) #remove all duplicates
    res = []
    
    def dfs(lst,state,currIndex,path,target):
        
        if state==target:
            res.append(path[:])
            return       
        
        for i in range(len(lst)):
            val = lst[i]
            if i>=currIndex and state+val > state and state+val<=target:
            #if state+i<=target:
                path.append(val)
                state+=val
                dfs(lst,state,i,path,target)
                state-=val
                path.pop()
        
    dfs(lst,0,0,[],total)
    print("---------------")
    print(res)            

                
    
    
     
    
def main():
    print("Permute list using dfs")
    lst1 = [1,2,3]
    printAllPermutations(lst1)
    lst1 = [1,2,2]
    printAllPermutationsNODups(lst1) #this requires a sorted input and does use map
    lst1 = [1,2,2]
    printAllPermutationsNODupsWithMap(lst1) #this uses map and is easy to understand
    lst1 = [1,2,3]
    getAllPermutations(lst1) #here [1,2] and [2,1] are allowed
    lst1 = [1,2,3,4]
    getAllUniqueCombinationsOfSizeLen(lst1, 3) #combination has unique values so [1,2,3] and [3,2,1] are same
    lst1 = [2,2,3]
    getAllUniqueCombinationsOfSizeLen(lst1,2) #this fails [2,3],[3,2] is output. Duplicate values are messing up the algo
    lst1 = [1,2,3]
    getDifferentWaystoAchieveATotal(lst1,5)
    lst1 = [-1,2,3]
    getDifferentWaystoAchieveATotal(lst1,5)
    lst1 = [1,2,3]
    getDifferentWaystoAchieveATotalNoDups(lst1,5) # here we do not allow [2,3] and [3,2] as they are same path
    
    
    
    
    
    
    
    
if __name__=="__main__":
    main()