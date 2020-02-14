import sqlite3
import pandas as pd

conn = sqlite3.connect('database/wine_data.sqlite')
df = pd.read_sql('SELECT * FROM wine_data', conn)
conn.close()


if __name__ == '__main__':
    [print(i) for i in df]