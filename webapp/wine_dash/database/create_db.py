import csv, sqlite3
import pandas as pd

conn = sqlite3.connect('wine_data.sqlite')
cur = conn.cursor()
columns = ['country', 'description', 'designation', 'points', 'price', 'province', 'region_1', 'region_2', 'variety', 'winery']
cur.execute(f'CREATE TABLE wine_data ({",".join(columns)})')

# data from https://www.kaggle.com/zynicide/wine-reviews
csv_file = 'winemag-data_first150k.csv'
df = pd.read_csv(csv_file, index_col=0)
df.to_sql('wine_data', conn, if_exists='append', index=False)
print(df.head())

conn.commit()
conn.close()