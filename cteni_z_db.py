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

# Načtení celé tabulky
cur.execute('SELECT * FROM lidi')
rows = cur.fetchall()

# Zobrazení výsledků
for row in rows:
    print(row)

conn.commit()  # Uložení změn
print('\n01. Změny byly uloženy')
# Uzavření kurzoru a spojení
cur.close()
print('02. Kurzor byl uzavřen')
conn.close()
print('03. Spojení uzavřeno')