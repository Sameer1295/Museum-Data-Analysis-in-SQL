import pandas as pd
from sqlalchemy import create_engine

conn_string = 'postgresql://postgres:root@localhost/museum_db'

db = create_engine(conn_string)
conn = db.connect()

files = ['artist','canvas_size','image_link','museum_hours','museum','product_size','subject','work']

for file in files:
    df = pd.read_csv(f'dataset_csvs/{file}.csv')
    # Check Dataset 
    # print(df.info)
    df.to_sql(file,con=conn,if_exists='replace',index=False)
print("Successfully created all tables!")