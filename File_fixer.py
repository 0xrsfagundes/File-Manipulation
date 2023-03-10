import pandas as pd

df = pd.read_csv("C://Users//rafael_fagundes//OneDrive - Dell Technologies//Documents//1153793_Untitled_Report_20230309_160522_4048829742.csv", on_bad_lines='skip', skiprows=10)

pd.set_option('display.max_columns', None)

df.to_csv("C://Users//rafael_fagundes//OneDrive - Dell Technologies//Desktop//GCM.csv")