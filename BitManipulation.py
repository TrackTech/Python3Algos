
def demarcate():
    print("\n")
    print("*" * 50)
    print("\n")

def main():
    print("Represent a number by its bits")
    n = 2
    print("n=2",bin(n))
    n=3
    print("n=3",bin(n))
    n=pow(2,3)
    print("n=",pow(2,3),bin(n))
    demarcate()

    print("Maximum number that can be accomodate in 3 bits")
    n = 0
    for i in range(3):
        n+=pow(2,i)
    print("3 1's equal to -",n)
    print("Checkout that is N+")
    n=0
    for i in range(4):
        n+=pow(2,i)
    print("4 1's equal to -",n)
    
    demarcate()

    print("For number in range 1 - 10 , not zero, we can store 8 number in 32")

    lst = [1,2,5,9,10]
    n = 0 # start with all zeros
    for num in lst:
        # push existing 1's in n to 4 places
        n=n<<4
        n|=num # here existing 1 will remain and trailing zeros become 1 for the bin representation of num
        print(n,bin(n))
    
    print(n,bin(n))
    demarcate()
    print("Check if num in in n after prior manipulation")
    print("Maximum size of n in bits would len(lst) * 4 -- 5 * 4 = 20")
    print("Caution: Use this approach only for 32 bits not more")








if __name__=="__main__":
    main()