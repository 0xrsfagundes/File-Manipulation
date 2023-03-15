from Regex_Test import *
import pandas as pd
import re

params = "FY23Q3_NA_UK|FY23AO_NA_FR"
params1 = "LIVERAMP"


df = pd.read_csv("C://Users//rafael_fagundes//OneDrive - Dell Technologies//Documents//1153793_Untitled_Report_20230309_160522_4048829742.csv", on_bad_lines='skip', skiprows=10)

pd.set_option('display.max_columns', None)

df_filtered = df[df["Placement"].str.contains(params)]
df_filtered = df_filtered.reset_index()

#Additional Filter
df_filtered1 = df_filtered[df_filtered["Placement"].str.contains(params1)]
df_filtered1 = df_filtered1.reset_index()

df_filtered1["Audience ID"] = ""

for index, row in df_filtered1.iterrows():
    df_filtered1.at[index,"Audience ID"] = getAudienceID(row["Placement"])

df_filtered1.to_csv("C://Users//rafael_fagundes//OneDrive - Dell Technologies//Desktop//filtered.csv")