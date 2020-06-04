import pandas as pd
from pandas_profiling import ProfileReport

#Reading a dataset
df = pd.read_csv('data.csv')

#Generate a report
profile = ProfileReport(df)
profile.to_file(output_file="index.html")