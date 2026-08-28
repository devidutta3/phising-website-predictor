import pandas as pd 
def extract_features(df):
    data=pd.DataFrame()
    data["url_length"]=df["url"].apply(len)
    data["num_dots"]=df["url"].apply(lambda x: x.count("."))
    print(df[["url" , "label"]]
          .head()
          )
    print(df["label"].value_counts())
    return data
df=pd.read_csv(r"data\\raw_data.csv")
features=extract_features(df)
print(features.head())