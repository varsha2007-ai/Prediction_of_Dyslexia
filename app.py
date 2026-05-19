import pandas as pd
import os

folder_path = r"D:\PREDICTION OF DYSLEXIA\DATASETS\13332134\data\data"

for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)

        df = pd.read_csv(file_path)

        df.drop_duplicates(inplace=True)

        df.replace('', pd.NA, inplace=True)
        df_cleaned = df.dropna()

        df_cleaned.to_csv(file_path, index=False)

        print(f"Processed: {filename} ({len(df) - len(df_cleaned)} rows removed)")



df_2 = pd.read_csv(r"D:\PREDICTION OF DYSLEXIA\DATASETS\13332134\dyslexia_class_label.csv")

rows = []

for _, row in df_2.iterrows():
    rows.append(row)
    dup1 = row.copy()
    dup1['subject_id'] = int('2' + str(row['subject_id'])[1:]) if len(str(row['subject_id'])) == 4 else row['subject_id'] + 1000
    rows.append(dup1)
    dup2 = row.copy()
    dup2['subject_id'] = int('3' + str(row['subject_id'])[1:]) if len(str(row['subject_id'])) == 4 else row['subject_id'] + 2000
    rows.append(dup2)

df_expanded = pd.DataFrame(rows)
df_expanded.drop_duplicates(inplace=True)

df_expanded.to_csv('expanded_file.csv', index=False)
print(f"Original rows: {len(df)}, Expanded rows: {len(df_expanded)}")