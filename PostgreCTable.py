import psycopg2

# Připojení k databázi
db_params = {
    'dbname': 'koyebdb',
    'user': 'koyeb-adm',
    'password': 'XQc0HOTwa1Kl',
    'host': 'ep-sweet-thunder-a221r1bm.eu-central-1.pg.koyeb.app',
    'port': 5432,
    'sslmode': 'require'
}
conn = psycopg2.connect(**db_params)

# Vytvoření kurzoru
cur = conn.cursor()

# Vytvoření tabulky
cur.execute('''
    CREATE TABLE IF NOT EXISTS test_table (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INTEGER
    )
''')
conn.commit()  # Uložení změn

# Uzavření kurzoru a spojení
cur.close()
conn.close()