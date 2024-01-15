from typing import List

def Quick_Select(nums:List[int],num:int)->int:
    """
    Given an unsorted list and a number n, give the index of n if the list were sorted
    
    Assumption: List values are distinct
    
    """
    # currIndex = -1
    # for i,n in enumerate(lst):
    #     if n==num:
    #         currIndex = i
    #         break
    
    # lst[currIndex],lst[len(lst)-1] = lst[len(lst)-1],lst[currIndex]

    # pivot = num # now at the last index

    # replaceIndex = 0

    # i = 0
    # while i<len(lst):
    #     if lst[i]<num:
    #         lst[i],lst[replaceIndex]=lst[replaceIndex],lst[i]
    #         replaceIndex+=1
    #     i+=1
    
    # return replaceIndex

    pivot = num
    replace_index = 0
    for i,n in enumerate(lst):
        if n<=pivot:
            nums[replace_index],nums[i]=nums[i],nums[replace_index]
            replace_index+=1
    
    return replace_index-1


if __name__=="__main__":
    print("Hello")
    lst = [5,1,4,0,2,3]
    print(lst,5,Quick_Select(lst,5))
    lst = [5,1,4,0,2,3]
    print(lst,2,Quick_Select(lst,2))
    lst = [5,1,4,0,2,3]
    print(lst,0,Quick_Select(lst,0))


