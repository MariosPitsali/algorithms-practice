import sqlite3
try:
  import tkinter
except ImportError:
  import Tkinter as tkinter

conn = sqlite3.connect("music.sqlite")
query = "SELECT name FROM albums WHERE artist = ? ORDER BY name"
cursor = conn.execute(query, (198, ))

for row in cursor:
  print(row)
  
conn.close()

