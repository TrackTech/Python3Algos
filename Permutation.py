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
    print(res)


def printAllPermutationsNODups(lst):
    res = []
    recurNumber= -1
    
    def dfs(lst,state,path,target):
        nonlocal recurNumber
        recurNumber+=1
        print("Recurrance:",recurNumber,", State:",state,", path:",path)
        if len(state)==target:
            res.append(path[:])
            print("Result-Recurrance:",recurNumber,", State:",state,", path:",path)
            return
        
        for i in range(len(lst)):
            if not i in state:
                if i>0 and lst[i]==lst[i-1] and i-1 in state:
                    print("declined entry:",i)
                    continue
                state.add(i)
                path.append(lst[i])
                dfs(lst,state,path,target)
                state.remove(i)
                path.pop()
                print("Pop-Recurrance:",recurNumber,", State:",state,", path:",path)
    
    lst.sort()
    dfs(lst,set([]),[],len(lst))
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
    print(res)

def substringThatSumToTarget():
    #substring is continous
    return
     
    
def main():
    print("Permute list using dfs")
    lst1 = [1,2,3]
    printAllPermutations(lst1)
    lst1 = [1,2,2]
    printAllPermutationsNODups(lst1) #this requires a sorted input and does use map
    lst1 = [1,2,2]
    printAllPermutationsNODupsWithMap(lst1) #this uses map and is easy to understand
    
    
    
if __name__=="__main__":
    main()