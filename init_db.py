import sqlite3

connection = sqlite3.connect('db.sqlite3')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Primeiro Post', 'Conteudo 1'))

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Conteudo 2')
            )

connection.commit()
connection.close()