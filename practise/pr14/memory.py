import sqlite3

db = sqlite3.Connection(":memory:")
sql = db.execute
sql("create table Students(name);")
sql("insert into Students values ('join');")

def add_name(name):
    cmd = f'insert into Students values ("{name}");'
    print("Executing:", cmd)
    db.executescript(cmd)
    print("Students:", sql("select * from Students;").fetchall())

def add_name_safe(name):
    sql("insert into Students values (?);", [name])
    print("Students:", sql("select * from Students;").fetchall())


# add_name("Jack")
# add_name("Jill")
# add_name("Robert'); DROP TABLE Students; --")
add_name_safe("Jack")
add_name_safe("Jill")
add_name_safe("Robert'); DROP TABLE Students; --")
