import random

bd_produtos = []

def adicionarProduto(codigo, produto, preco):
    prod = {
        'codigo': codigo,
        'produto': produto,
        'preco' : preco
    }
    bd_produtos.append(prod)
    print('Produto cadastrado com sucesso!')
def editarProduto(codigo,produto,preco):
    for prod in bd_produtos:
        if prod['codigo'] == codigo:
            prod ['produto'] = produto
            prod ['preco'] = preco
            print('Dados alterados com sucesso!')
def pesquisarProduto(codigo):
    encontrado = False
    for produto in bd_produtos:
        if produto["codigo"] == codigo:
            print(f"Código: {produto['codigo']}")
            print(f"Produto: {produto['produto']}")
            print(f"Preco: {produto['preco']}")
            print('---------------------')
            encontrado = True

    if not encontrado:
        print('Produto não encontrado')

def deletarProduto(codigo):
    encontrado = False
    for produto in bd_produtos:
        if produto['codigo'] == codigo:
            bd_produtos.remove(produto)
            print("Produto deletado com sucesso!")
            encontrado = True

    if not encontrado:
        print("Produto não encontrado")

while True:
    print("------ Bem vindo ao Menu ------")
    opcao = int(input("1 - Adicionar produto \n"
                      "2 - Editar produto \n"
                      "3 - Pesquisar produto \n"
                      "4 - Deletar produtos \n"
                      "5 - Listar todos \n"
                      "6 - Sair \n"
                      "Selecione uma opção: "))

    if opcao == 1:
        cod = random.randint(1,1000)
        produto = input('Digite o nome do produto')
        preco = float(input('Digite o preço do produto: '))
        adicionarProduto(cod,produto,preco)
    elif opcao == 2:
        cod = int(input('Digite o código do produto'))
        produto = input('Digite o nome do produto')
        preco = float(input('Digite o preço do produto: '))
        editarProduto(cod,produto,preco)
    elif opcao == 3:
        cod = int(input('Digite o código do produto'))
        pesquisarProduto(cod)
    elif opcao == 4:
        cod = int(input('Digite o código do produto'))
        deletarProduto(cod)
    elif opcao == 5:
        print(bd_produtos)
    elif opcao == 6:
        break
