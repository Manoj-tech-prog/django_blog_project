import psycopg2

conn = psycopg2.connect(host='localhost', dbname='Practice', user='postgres',
                        password='root')

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS person (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        gender TEXT
    )
""")

# Insert data into the table
cur.execute("""
    INSERT INTO person (name, age, gender) VALUES
    ('manoj', 30, 'male'),
    ('osee', 40, 'female'),
    ('john', 20, 'male'),
    ('christy', 50, 'female');
""")


conn.commit()
cur.close()
conn.close()