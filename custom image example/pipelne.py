# Necessary libraries
import pandas as pd
import requests

#URL with data source
url = "https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv"

#Get data from the URL and stroe it in a pandas DataFrame
df = pd.read_csv(url)

# Data cleaning and transformation
df = df.dropna()
df = df[df["confirmed"] > 0]

#Save cleaned data in a new csv file
df.to_csv("cleaned_data.csv", index=False)