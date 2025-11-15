import sqlite3

conn = sqlite3.connect("banco.db")

cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE produtos (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        preco INTEGER,
        detalhes TEXT
    )
    """
)

def preco_para_banco(prec):
    preco = int(prec * 100 )
    return preco

def preco_para_soft(prec):
    preco = float(prec)/100
    return preco