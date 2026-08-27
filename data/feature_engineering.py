import pandas as pd 
def extract_features(df):
    data=pd.DataFrame()
    data["url_length"]=data["url"].apply(len)

    return data

df=pd.read_csv(r"data\raw_data.csv")
