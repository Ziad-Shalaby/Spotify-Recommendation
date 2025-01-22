import sqlite3
import pandas as pd

db_path = 'spotify_songs.db'
conn = sqlite3.connect(db_path)

query = "SELECT * FROM songs"  
df = pd.read_sql_query(query, conn)

conn.close()

print(df)
df.to_csv('songs.csv')