import pandas as pd

def data(range_data):
    df=pd.read_csv(r"data\raw_data.csv")
    return df.head(range_data)

if __name__=="__main__":
    range_data=int(input("Enter The Number To Print First:"))
    result = data(range_data)
    print(result)
    print("DataSet Shape :",result.shape)
    print("\nMissing Values:")
    print(result.isnull().sum())
    print("\n Duplicate Url:")
    print(result["url"].duplicated().sum())
    print("\nClass Distribution:")
    print(result["label"].value_counts())
    print("\nClass Percentage:")
    print(result["label"].value_counts(normalize=True) * 100)

    