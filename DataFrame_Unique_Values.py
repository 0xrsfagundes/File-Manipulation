import pandas as pd
import warnings

file_path = "C://Users//rafael_fagundes//OneDrive - Dell Technologies//Desktop//GCM.csv"
save_path = "C://Users//rafael_fagundes//OneDrive - Dell Technologies//Desktop//GCM_unique.csv"
encoding = 'utf8'

with warnings.catch_warnings(record=True):
    warnings.simplefilter("always")
    df = pd.read_csv(file_path, encoding=encoding)

unique_values = {}

for column in df.columns:
    unique_values[column] = df[column].unique()


unique_df = pd.DataFrame.from_dict(unique_values, orient='index').transpose()

unique_df.to_csv(save_path)