import sqlite3
import tabulate as tab
import csv

connect = sqlite3.connect('database.db')
c = connect.cursor()


def cretedb():
    c.execute("DROP TABLE IF EXISTS 'Cars'")
    c.execute("DROP TABLE IF EXISTS 'Owners'")

    c.execute("""
    CREATE TABLE Cars(
    Id INTERGER NOT NULL PRIMARY KET AUTOUNCREMENT,
    
    
    )
    """)

    c.execute("""
    
    """)