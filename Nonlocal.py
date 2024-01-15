import sys
def sum():
    stack = []
    def inner():
        stack.append(1)
        print(stack)
    inner()



def main():
    print("hello")
    sum()
    print(sys.version)

if __name__=="__main__":
    main()
