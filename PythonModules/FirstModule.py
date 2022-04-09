
def first(num:int):
    return num+1

if __name__=="__main__":
    import sys
    print("This module can also be called from terminal using command")
    print("python3 FirstModule.py 100")
    x = first(int(sys.argv[1]))
    print(x)

