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

# Načtení celé tabulky
cur.execute('SELECT * FROM test_table')
rows = cur.fetchall()

# Zobrazení výsledků
for row in rows:
    print(row)

# Uzavření kurzoru a spojení
cur.close()
conn.close()