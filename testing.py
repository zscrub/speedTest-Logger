import sqlite3
import pandas as pd
from sqlalchemy import create_engine

file = "speedTestsDB.xlsx"
engine = create_engine('sqlite://', echo=False)
df = pd.read_excel(file, sheet_name='speedTests')

results = engine.execute("SELECT * FROM speedTests")

path = os.path.basename(r"C:\Users\xacc\Desktop\speedTestsDB.xlsx")

final = pd.DataFrame(results,columns=df.columns)
# final.to_excel(file, index=False)