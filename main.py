import bd

produto = {
    "nome": "Paçoca Rolha",
    "preco": 1.50,
    "detalhes": "Paçoquinha rolha extremamente seca"
}

#bd.create("Chocolate Belga", 23.80, "Chocolate que nunca comi mas ouço falar")

#print(bd.read(3))

# bd.update(2, "Chocolate Barato", 1.50, "Chocolate que sempre comi")

# print(bd.read(2))

bd.delete(2)

print(bd.read())