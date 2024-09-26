import pandas as pd
import sqlite3

data = pd.DataFrame({
    'ID': [2, 4, 6, 8],
    'Name': ['Alyssa', 'Cadu', 'Lili', 'Guga']
})

conn = sqlite3.connect('mydatabase.db')


data.to_sql(
    'client', conn,
    if_exists='replace',
    index=False
)

conn.close()

conn = sqlite3.connect('mydatabase.db')

query = """ 
    SELECT Name 
    FROM client
    WHERE name IN ('Alyssa', 'Guga')
"""

pd.read_sql_query(query, conn)
