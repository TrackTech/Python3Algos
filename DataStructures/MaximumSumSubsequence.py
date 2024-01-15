
def main(lst=None):
    if not lst:
        lst = [-1,-2,0,1,2]

    lstMax = max(lst)

    if lstMax<=0:
        return lstMax
    sum=0
    for n in lst:
        if n>0:
            sum+=n
    
    return sum

if __name__=="__main__":
    print(main())
    lst = [-1,-2,-3,-9]
    print(main(lst))