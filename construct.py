import sqlite3
from sqlite3.dbapi2 import OperationalError;

conn = sqlite3.connect('database.db'); 
with open('construct.sql',encoding = 'utf-8') as f:
    conn.executescript(f.read());
    f.close();
cur = conn.cursor();
cur.execute('INSERT INTO posts (title, content) VALUES (?,?)',("Test1","Test"));
cur.execute('INSERT INTO posts (title, content) VALUES (?,?)',("Test1","Test"));

conn.commit();
conn.close();

    
