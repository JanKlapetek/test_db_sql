import psycopg2

# Připojení k databázi
db_params = {
    'dbname': 'sandbox',
    'user': 'koyeb-adm',
    'password': 'RmiEvoMz7a3s',
    'host': 'ep-white-band-a2h03cgc.eu-central-1.pg.koyeb.app',
    'port': 5432,
    'sslmode': 'require'
}
conn = psycopg2.connect(**db_params)

# Vytvoření kurzoru
cur = conn.cursor()

# Vytvoření tabulky
cur.execute('''
    CREATE TABLE IF NOT EXISTS lidi (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INTEGER
    )
''')

# Vytvoření tabulky
cur.execute('''
    CREATE TABLE IF NOT EXISTS lidi (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INTEGER
    )
''')

# Vložení dat
lidi_data = [
    ('Jan Novak', 34),
    ('Petra Svobodova', 28),
    ('Karel Dvorak', 45),
    ('Martina Novakova', 30),
    ('Lukas Polak', 25)
]


cur.executemany('''
    INSERT INTO lidi (name, age) VALUES (%s, %s)
''', lidi_data)


conn.commit()  # Uložení změn
print('01. Změny byly uloženy')
# Uzavření kurzoru a spojení
cur.close()
print('02. Kurzor byl uzavřen')
conn.close()
print('03. Spojení uzavřeno')