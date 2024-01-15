import pandas as pd
import numpy as np
import typing

class Person:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    
def main():
    print("In Main")
    people:List[Person]=[]

    for i in range(10):
        p = Person(
            i,"Rushikesh","M"
        )
        people.append(p)
    peopleList = [[p.name,p.age,p.sex] for p in people]
    people_np = np.array(peopleList)
    df = pd.DataFrame(people_np)
    df.to_csv("Export1.csv")
    print(df)
    print("Done")


if __name__=="__main__":
    main()