import sqlite3
bd=sqlite3.connect('user.db')
sql=bd.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS user(
login TEXT,
password TEXT
)""")
bd.commit()
def reg():
    user_login = input("Log in:")
    user_password = input("Pass: ")
    sql.execute(f"SELECT login FROM user WHERE login ='{user_login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO user VALUES(?,?)", (user_login, user_password))
        bd.commit()
        print("Succeful")
    else:
        print("Error")
        for i in sql.execute("SELECT * FROM user"):
            print(i)
def login():
    user_login=input("Log in: ")
    sql.execute(f"SELECT login FROM user WHERE login ='{user_login}'")
    if sql.fetchone() is None:
        print("Please reg")
        reg()
    else:
        user_password = input("Pass: ")
        sql.execute(f"SELECT password FROM user WHERE password ='{user_password}'")
        if sql.fetchone() is None:
            print("Error")
        else:
            print("Welcome!")
login()