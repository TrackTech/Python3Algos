
def quick_select(lst,l,r):
    
    replaceIndex = l
    pivot = lst[r]
    # pivot and replace index are on opposite ends
    i = l
    while i<r+1:
        if lst[i]<=pivot: # remember the equal sign
            lst[i],lst[replaceIndex]=lst[replaceIndex],lst[i]
            replaceIndex+=1
        i+=1
    print(l,r,replaceIndex)
    return replaceIndex-1

def testPivot(lst,k=2):


    # find 3rd smallest index
    l = 0
    r = len(lst)-1

    while True:
        pivot_index = quick_select(lst,l,r)
        
        if pivot_index==k:
            print("Done--",lst[k])
            break

        if pivot_index>k:
            r = pivot_index-1
        else:
            l=pivot_index+1



def main():
    lst = [5,0,1,3,2,4]
    testPivot(lst,2)
    lst = [10,8]
    testPivot(lst,1)
    lst = [10,8]
    testPivot(lst,0)
    

if __name__=="__main__":
    main()

    