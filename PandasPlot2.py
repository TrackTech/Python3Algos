import pandas as pd
import matplotlib as md

def main():
   
    data_type = {
        'Id':'int64',
        'Name':'object', ### STRING is represented by Object
        'Age':'int64',
        ### Datetime is not included here, parse_dates is used
    }

    df3 = pd.read_csv("./train3.csv",names=["Id","Name","Age","DOB"],dtype=data_type,parse_dates=["DOB"]) # checkout parse dates

    print(df3.describe)

    df3.sort_values(by=["Name","Age"],ascending=[False,True],inplace=True)
    print(df3)
    print("Print the max value of age-",df3["Age"].max())
    print("Add a new column - diff age")
    df3["Age_Max_Diff"]=df3["Age"].max() - df3["Age"]
    print(df3)

if __name__=="__main__":
    main()