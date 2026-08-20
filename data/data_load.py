import pandas as pd

def data(range_data):
    df=pd.read_csv(r"data\raw_data.csv")
    return df.head(range_data)

if __name__=="__main__":
    range_data=int(input("Enter The Number To Print First:"))
    result = data(range_data)
    print(result)

    