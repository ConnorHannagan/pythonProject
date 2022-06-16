import sqlite3
import tablulate as tab
connect = sqlite3.connect('database.db')
c = connect.cursor()


def createdb():
    print("Creating DB...")

    c.execute("DROP TABLE IF EXISTS 'Books'")
    c.execute("DROP TABLE IF EXISTS 'Owners'")
    c.execute("DROP TABLE IF EXISTS 'BO'")

    c.execute("""CREATE TABLE Books(
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name NOT NULL
    );
    """)

    c.execute("""CREATE TABLE Owners(
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name NOT NULL
    );
    """)
    c.execute("""CREATE TABLE BO(
    Bookid NOT NULL,
    Ownerid NOT NULL,
    FOREIGN KEY (Bookid) REFERENCES Books(Id),
    FOREIGN KEY (Ownerid) REFERENCES Owners(Id)
    );
    """)

    c.execute(""" INSERT INTO Books(Name) VALUES
    ('Harry potter'),
    ('To kill a mocking bird'),
    ('Lord of the rings'),
    ('I am not esther')
    """)

    c.execute("""INSERT INTO Owners(Name) Values
    ('Tom'),
    ('Jerry'),
    ('Adam'),
    ('Kathryn'),
    ('Millie'),
    ('Lisa')
    """)

    c.execute("""INSERT INTO BO(Ownerid, Bookid) VALUES
    ('1','1'),
    ('1','4'),
    ('2','1'),
    ('2','2'),
    ('2','3'),
    ('3','4'),
    ('4','1'),
    ('5','1'),
    ('6','2'),
    ('6','1'),
    ('6','1'),
    ('6','1')
    """)
    input("DB Created Enter to continue : ")
    print("\n"*20)

createdb()
while True:
    userinput = input("1, view books\n2, view People\n3, view Books and people\n")
    if userinput == "1":
        c.execute("SELECT Books.Name FROM Books")
        headers = "Name"
        print(tab.tabulate(c.fetchall(), headers, tablefmt='simple'))


    elif userinput == "2":
        c.execute("Select Owners.Name FROM OWNERS")
        input(c.fetchall())


    elif userinput == "3":
        c.execute(""" SELECT Books.Name, Owners.Name
           FROM BO
           INNER JOIN Books ON Books.Id = BO.Bookid
           INNER JOIN Owners ON Owners.Id = BO.Ownerid
           """)
        input(c.fetchall())


    else:
        input("not Valid input")
    print("\n"*20)



connect.commit()
connect.close()