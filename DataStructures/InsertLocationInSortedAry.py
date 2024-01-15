lst = [1,2,3,4]



def insert_location(lst,x)->int:
    left = 0
    right = len(lst)-1
    while left<=right:
        mid = (left+right)//2
        if lst[mid]==x:
            return mid
        if lst[mid]<x:
            left=mid+1
        else:
            right=mid-1
    return left

lst = [1,2,3,4]
x = 2
print(insert_location(lst,x))

lst = [1,2,3,4]
x = -1
print(insert_location(lst,x))

lst = [1,2,3,4]
x = 5
print(insert_location(lst,x))
