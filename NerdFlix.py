from datetime import date, datetime
from hmac import compare_digest
from math import prod
from time import strftime
from tkinter.tix import InputOnly
from wsgiref.validate import validator
#produtos
class product:
    def __init__(self, nome, codigo, preco, tipo, disponivel):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        self.tipo = tipo
        self.disponivel = disponivel

nome_produto = ['filme1', 'filme2']
codigo_produto = [1, 2]
preco_produto = [25.3, 43.1]
tipo_produto = [2, 5]
disponivel_produto = ['Disponível', 'Indisponível']
lista4 = []
lista_de_confirm = []

#mostra o produto com todos os dados
def verificacao():
    verificacao = int(input("Produto à ser verificado: "))
    lista4.append(codigo_produto[verificacao-1])
    lista4.append(nome_produto[verificacao-1])
    lista4.append(preco_produto[verificacao-1])
    lista4.append(tipo_produto[verificacao-1])
    lista4.append(disponivel_produto[verificacao-1])
    print(lista4)
    iniciar()

#cadastrar produtos
def cadastro():
    numero_de_cadastros = int(input("Número de produtos a serem cadastrados: "))

#Trocar while por nova chamada de função / // /
    while numero_de_cadastros > 0:
        product.nome = str(input("\nNome: "))
        product.preco = float(input("Preço: "))
        product.tipo = int(input("Tipo: "))
        if product.tipo == 1:
            product.tipo = "Série"
        elif product.tipo == 2:
            product.tipo = "Filme"
        elif product.tipo == 3:
            product.tipo == "Documentário" 
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
    iniciar()

#consulta por classe
def consulta():
    indice = -0
    print("0 - Todos os produtos\n1 - Somente filmes\n2 - Séries\n3 - Documentários\n4 - Todos os produtos disponíveis\n5 - Todos os produtos indisponíveis")
    opcao = int(input("\nFiltro: "))    
    if opcao == 0:
        for x in tipo_produto:
            print(f"{codigo_produto[indice]}, {nome_produto[indice]}, R${preco_produto[indice]}, {tipo_produto[indice]}, {disponivel_produto[indice]}")
            indice += 1
    elif opcao == 1:
        for y in tipo_produto:
            if y == 2:
                print(f"{codigo_produto[indice]}, {nome_produto[indice]}, R${preco_produto[indice]}, {tipo_produto[indice]}, {disponivel_produto[indice]}")
            indice += 1
    elif opcao == 2:
        for x in tipo_produto:
            if x == 1:
                print(f"{codigo_produto[indice]}, {nome_produto[indice]}, R${preco_produto[indice]}, {tipo_produto[indice]}, {disponivel_produto[indice]}")
            indice += 1
    elif opcao == 3:
        for x in tipo_produto:
            if x == 3:
                print(f"{codigo_produto[indice]}, {nome_produto[indice]}, R${preco_produto[indice]}, {tipo_produto[indice]}, {disponivel_produto[indice]}")
            indice += 1
    elif opcao == 4:
        for x in disponivel_produto:
            if x == "Disponível":
                print(f"{codigo_produto[indice]}, {nome_produto[indice]}, R${preco_produto[indice]}, {tipo_produto[indice]}, {disponivel_produto[indice]}")
            indice += 1

    elif opcao == 5:
        for x in disponivel_produto:
            if x == "Indisponível":
                print(f"{codigo_produto[indice]}, {nome_produto[indice]}, R${preco_produto[indice]}, {tipo_produto[indice]}, {disponivel_produto[indice]}")
            indice += 1
    print("\nA consulta foi concluída")
    iniciar()

#atualiza produtos    
def atualizar():
    remover = int(input("índice: "))
    lista_de_confirm.append(codigo_produto[remover-1])
    lista_de_confirm.append(nome_produto[remover-1])
    lista_de_confirm.append(tipo_produto[remover-1])
    lista_de_confirm.append(disponivel_produto[remover-1])
    print(lista_de_confirm)
    confirm = int(input("1 - confirmar \n2 - cancelar"))
    if confirm == 1:
        nome_produto.remove(nome_produto[remover-1])
        disponivel_produto.remove(disponivel_produto[remover-1])
        tipo_produto.remove(tipo_produto[remover-1])
        nome_produto.remove(nome_produto[remover-1])
        if len(codigo_produto) > len(nome_produto):
            for i in range(0, len(codigo_produto), -1):
                codigo_produto.remove(codigo_produto[i])
                print(codigo_produto)
        #pede os novos parâmetros
        product.nome = str(input("\nNome: "))
        product.preco = float(input("Preço: "))
        product.tipo = int(input("Tipo: "))
        product.disponivel = str(input("Disponivel(s/n): "))
        #os organiza no indice na lista
        nome_produto.insert(len([remover-1]), product.nome)
        preco_produto.insert(len([remover-1]), product.preco)
        tipo_produto.insert(len([remover-1]), product.tipo) 
        disponivel_produto.insert(len([remover-1]), product.disponivel)
    iniciar()

#registra compra
def registrar_compra():
    global login
  ##  compra = []
    login = input("Insira seu login: ")

    while True:          
        cod_conf = int(input("Digite o código do produto: "))
        if cod_conf == -1:
            break
        while cod_conf != 1 and cod_conf != 2 and cod_conf != 3:
            cod_conf = int(input("Código inválido, tente novamente: "))
        print(cod_conf)
        confirmar_compra = int(input("1 - Confirmar\n2 - Cancelar")) 
        if confirmar_compra == 1:
            print()
           #### compra.append()
        else:
            cod_conf = int(input("Digite o código do produto: "))
        time()

def relatorio():
    print(login, data)
    print("Código   Nome   Tipo   Preço")
    print()


#data e hora:
def time():
    global data
    agora = datetime.now()
    data = agora.strftime("%d/%m/%Y %H:%M:%S")
    print(data)

#inicia o programa:

def iniciar():

    #mensagem inicial e verificação de códigox' 

    print("1 - Cadastrar\n2 - Consultar\n3 - Atualizar\n4 - Pesquisar\n5 - Registrar Compra\n6 - Relatório de compras")
    method = int(input("\nDigite sua ação: "))

    if method == 1:
        cadastro()
    elif method == 2:
        consulta()                  
    elif method == 3:
        atualizar()
    elif method == 4:
        verificacao()
    elif method == 5:
        registrar_compra()
    elif method == 6:
        relatorio()
iniciar()

time()
