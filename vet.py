from math import prod


class product:
    def __init__(self, nome, codigo, preco, tipo, disponivel):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        self.tipo = tipo
        self.disponivel = disponivel

nome_produto = []
codigo_produto = []
preco_produto = []
tipo_produto = []
disponivel_produto = []


#Método de cadastro
def cadastro(method):
    if method == 2:
        numero_de_cadastros = int(input("Número de produtos a serem cadastrados: "))

#Trocar while por nova chamada de função / // /
        while numero_de_cadastros > 0:
            product.nome = str(input("\nNome: "))
            product.preco = float(input("Preço: "))
            product.tipo = int(input("Tipo: "))
            product.disponivel = str(input("Disponivel(s/n): "))
            if product.disponivel == "s":
                product.disponivel = "Disponível"
            elif product.disponivel == "n":
                product.disponivel = "Indisponível"
            nome_produto.append(product.nome)
            preco_produto.append(product.preco)
            tipo_produto.append(product.tipo)
            disponivel_produto.append(product.disponivel)
            codigo_produto.append(len(nome_produto))
            
            
            numero_de_cadastros = numero_de_cadastros - 1 
            
            print(codigo_produto, nome_produto, preco_produto, tipo_produto, disponivel_produto)

#simulação de produtos cadastrados

lista4 = []
lista_de_confirm = []

#Método de remoção ()
def remover(method):
    if method == 1:
        remover = int(input("índice: "))
        lista_de_confirm.append(product.nome[remover-1])
        lista_de_confirm.append(product.codigo[remover-1])
        lista_de_confirm.append(product.disponivel[remover-1])
        print(lista_de_confirm)
        confirm = int(input("1 - confirmar \n2 - cancelar"))
        if confirm != int:
            confirm = int(input("1 - confirmar \n2 - cancelar"))
        if confirm == 1:
            product.nome.remove(product.nome[remover-1])
            product.disponivel.remove(product.disponivel[remover-1])
            if len(product.nome) > len(product.nome):
                for i in range(0, len(product.codigo), -1):
                    product.codigo.remove(product.codigo[i])
                    print(product.codigo)

#verifica um produto cadastrado pelo código
def verificacao():
    verificacao = int(input("Produto à ser verificado: "))
    lista4.append(codigo_produto[verificacao-1])
    lista4.append(nome_produto[verificacao-1])
    lista4.append(preco_produto[verificacao-1])
    lista4.append(tipo_produto[verificacao-1])
    lista4.append(disponivel_produto[verificacao-1])
    print(lista4)

method = int(input("1 - Remover\n2 - cadastro\n"))

#Criar loop de funções / // /

remover(method)

cadastro(method)

verificacao()