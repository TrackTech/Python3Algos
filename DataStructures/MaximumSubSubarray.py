def main(lst=None):
    if not lst:
        lst = [-1,-2,0,1,2]

    currSum = lst[0]
    maxSum = lst[0]

    # increase the currSum only when currSum+n>n

    for i,n in enumerate(lst):
        if i==0:
            continue
        if currSum+n>n:
            currSum+=n
        else:
            currSum=n
        maxSum = max(maxSum,currSum)
    
    return maxSum

if __name__=="__main__":
    print(main())
    lst = [-1,-2,-3,-9]
    print(main(lst))
    lst = [1,2,3,9]
    print(main(lst))