from datetime import date, datetime
import pandas as pd

#produtos
class product:
    def __init__(self, nome, codigo, preco, tipo, disponivel):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        self.tipo = tipo
        self.disponivel = disponivel

detalhes = []
codigo_comprado = []
nome_comprado = []
preco_comprado = []
tipo_comprado = []
lista_de_verif = []
lista_de_confirm = []
product.codigo = 0
#mostra o produto com todos os dados
def verificacao():
    verificar = input("Produto à ser verificado: ")
    while True: 
        try:
            verificar = int(verificar)
            break
        except:
            verificar = input("Formato inválido, tente novamente: ")

    for i in range(len(detalhes)):
        if detalhes[i].codigo == verificar:
            print(f"{detalhes[i].codigo}, {detalhes[i].nome}, R${detalhes[i].preco}, {detalhes[i].tipo}, {detalhes[i].disponivel}")

        while detalhes[i].codigo != verificar:
            verificar = input("Produto inexistente, tente novamente: ")
    iniciar()
#cadastrar produtos
def cadastro():
    print("Cadastro de produtos:")
    while True:
        product.nome = input("\nNome: ")
        if product.nome == '':
            break

        product.preco = input("Preço: ")
        while True:    
            try:
                product.preco = float(product.preco)
                break
            except:
                product.preco = input("Formato inválido, digite o preço novamente: ")

        product.tipo = input("Tipo: ")
        while product.tipo != "1" and product.tipo != "2" and product.tipo != "3":
            product.tipo = input("Formato inválido, digite o tipo novamente: ")
        product.tipo = int(product.tipo)

        product.disponivel = input("Disponível(s/n): ")
        while product.disponivel != "s" and product.disponivel != "n":
            product.tipo = input("Formato inválido, digite novamente(s/n): ")

        product.codigo += 1

        if product.tipo == 1:
            product.tipo = "Série"
        elif product.tipo == 2:
            product.tipo = "Filme"
        elif product.tipo == 3:
            product.tipo == "Documentário" 
        if product.disponivel == "s":
            product.disponivel = "Disponível"
        elif product.disponivel == "n":
            product.disponivel = "Indisponível"
        detail = product(product.nome, product.codigo, product.preco, product.tipo, product.disponivel)
        detalhes.append(detail)
        
        print(f"{detail.codigo}, {detail.nome}, R${detail.preco}, {detail.tipo}, {detail.disponivel}")
    iniciar()

#atualiza produtos    
def atualizar():
    #pede os novos parâmetros
    verificar = input("Produto à ser verificado: ")
    while True: 
        try:
            verificar = int(verificar)
            break
        except:
            verificar = input("Formato inválido, tente novamente: ")

    for i in range(len(detalhes)):
        if detalhes[i].codigo == verificar:
            print(f"{detalhes[i].codigo}, {detalhes[i].nome}, R${detalhes[i].preco}, {detalhes[i].tipo}, {detalhes[i].disponivel}")

        while detalhes[i].codigo != verificar:
            verificar = input("Produto inexistente, tente novamente: ")

    print("1 - Atualizar nome\n2 - Atualizar preço\n3 - Atualizar Tipo\n4 - Atualizar disponibilidade")
    metodat = input("Método de atualização: ")
    while metodat != "1" and metodat != "2" and metodat != "3" and metodat != "4": 
        metodat = input("Método inválido, digite novamente: ")

    confirmacao = input("\nConfirmação(s/n): ")
    if confirmacao != "s" and confirmacao != "n":
        confirmacao = input("Formato inválido, digite a confirmação novamente: ")
    
    if confirmacao == "n":
        atualizar()
    
    while confirmacao != 's' and confirmacao != 'n':
        confirmacao = input("Método inválido, digite novamente: ")

    if metodat == "1" and confirmacao == "s":
        product.nome = input("\nNome: ")

        for i in range(len(detalhes)):
            detalhes[i].nome = product.nome
         
    elif metodat == "2" and confirmacao == "s":
        product.preco = input("Preço: ")
        while True:    
            try:
                product.preco = float(product.preco)
                break
            except:
                product.preco = input("Formato inválido, digite o preço novamente: ")

        for i in range(len(detalhes)):
            detalhes[i].preco = product.preco

    elif metodat == "3" and confirmacao == "s":
        product.tipo = input("Tipo: ")

        while product.tipo != "1" and product.tipo != "2" and product.tipo != "3":
            product.tipo = input("Formato inválido, digite o tipo novamente: ")

        for i in range(len(detalhes)):
            detalhes[i].tipo = product.tipo

    elif metodat == "4" and confirmacao == "s":
        product.disponivel = input("Disponibilidade(s/n): ")

        while product.disponivel != "s" and product.disponivel != "n":
            product.tipo = input("Formato inválido, digite novamente(s/n): ")

        if product.disponivel == "s":
            product.disponivel = "Disponível"
        elif product.disponivel == "n":
            product.disponivel = "Indisponível"
        

        for i in range(len(detalhes)):
            detalhes[i].disponivel = product.disponivel
    iniciar()

#registra compra
def registrar_compra():
    global login
  ##  compra = []
    login = input("Insira seu login: ")
    while login == '':
        login = input("Insira seu login: ")

    while True:          
        cod_conf = input("Digite o código do produto: ")
        for i in range(len(detalhes)):
            while i+1 != detalhes[i].codigo:
                cod_conf = input("Código inválido, tente novamente: ")
        if cod_conf == '':
            break
        print(cod_conf)
        print("1 - Confirmar\n2 - Cancelar")
        confirmar_compra = input("Método: ")
        while confirmar_compra != '1' and confirmar_compra != '2':
            confirmar_compra = input("Método inválido, digite novamente: ") 
        if confirmar_compra == '1':
            codigo_comprado.append(cod_conf)
        else:
            cod_conf = input("Digite o código do produto: ")
        time()
    iniciar()

def relatorio_produtos():
    print("0 - Todos os produtos\n1 - Somente filmes\n2 - Séries\n3 - Documentários\n4 - Todos os produtos disponíveis\n5 - Todos os produtos indisponíveis")
    opcao = input("\nFiltro: ")
    while opcao != "0" and opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "5":
        opcao = input("Filtro inválido, tente novamente: ")
 
    if opcao == '0':
        for i in range(len(detalhes)):
            print(f"{detalhes[i].codigo}, {detalhes[i].nome}, R${detalhes[i].preco}, {detalhes[i].tipo}, {detalhes[i].disponivel}")
            
    elif opcao == '1':
        for i in range(len(detalhes)):
            if detalhes[i].tipo == 2:
                print(f"{detalhes[i].codigo}, {detalhes[i].nome}, R${detalhes[i].preco}, {detalhes[i].tipo}, {detalhes[i].disponivel}")

    elif opcao == '2':
        for i in range(len(detalhes)):
            if detalhes[i].tipo == 1:
                print(f"{detalhes[i].codigo}, {detalhes[i].nome}, R${detalhes[i].preco}, {detalhes[i].tipo}, {detalhes[i].disponivel}")
            
    elif opcao == '3':
        for i in range(len(detalhes)):
            if detalhes[i].tipo == 3:
                print(f"{detalhes[i].codigo}, {detalhes[i].nome}, R${detalhes[i].preco}, {detalhes[i].tipo}, {detalhes[i].disponivel}")

    elif opcao == '4':
        for i in range(len(detalhes)):
            if detalhes[i].disponivel == "Disponível":
                print(f"{detalhes[i].codigo}, {detalhes[i].nome}, R${detalhes[i].preco}, {detalhes[i].tipo}, {detalhes[i].disponivel}")
            0
    elif opcao == '5':
        for i in range(len(detalhes)):
            if detalhes[i].disponivel == "Indisponível":
                print(f"{detalhes[i].codigo}, {detalhes[i].nome}, R${detalhes[i].preco}, {detalhes[i].tipo}, {detalhes[i].disponivel}")
    
    print("\nA consulta foi concluída")
    iniciar()
    
def relatorio_compras():

    print(login, data)
    for x in range(len(detalhes)):
        for i in codigo_comprado:
            if detalhes[x].codigo == i:
                nome_comprado.append(detalhes[i].nome)
                preco_comprado.append(detalhes[i].preco)
                tipo_comprado.append(detalhes[i].tipo)
        
    tabelas = {'Código': [codigo_comprado],
    'Nome': [nome_comprado],
    'Preço': [preco_comprado],
    'Tipo': [tipo_comprado]}
    
    tabela = pd.DataFrame(tabelas)
    
    print(tabela)

#data e hora:
def time():
    global data
    agora = datetime.now()
    data = agora.strftime("%d/%m/%Y %H:%M:%S")
    print(data)

#inicia o programa:

def iniciar():

    #mensagem inicial e verificação de códigox' 

    print("1 - Cadastrar\n2 - Consultar\n3 - Atualizar\n4 - Registrar Compra\n5 - Relatório de produtos\n6 - Relatório de compras")
    method = input("\nDigite sua ação: ")
    while method != '1' and method != '2' and method != '3' and method != '4' and method != '5' and method != '6':
        method = input("\nFormato inválido, digite sua ação novamente: ")

    if method == "1":
        cadastro()
    elif method == "2":
        verificacao()
    elif method == "3":
        atualizar()
    elif method == "4":
        registrar_compra()
    elif method == "5":
        relatorio_produtos()
    elif method == "6":
        relatorio_compras()

iniciar()
time()