# Esse codigo ira criar um menu improvisado, o mesmo  sera executado no terminal

# OBS : sempre antes de rodar o codigo  tem que cadastrar um produto , pois o programa nao
# tem banco de dados para salvar o que foi cadastrado antes de fechar 
                                                    
def personalizado(txt, itens, *chamadas):
    print('-=-' * 18)
    print(txt.center(47))
    print('-=-' * 18)
    print()
    for c in range(0, itens):
        print(f'{c +1} - {chamadas[c]}')
def listarprodutos():
    for i in range(0, len(produtos)):
        print("Produto: {} - {} - R${:.2f} - Quantidade em estoque:  {}".format(i, produtos[i][0], produtos[i][1], produtos[i][2]))
produtos = []
while True: # Responsavel por manter o loop do programa rodando
     
    # Personalizado(O nome do menu , a quantidade de opcoes do menu, opcao 1 , opcao 2 , opcao 3 , opcao 4 )
    personalizado('Sistema de venda', 4, 'Cadastra produtos', 'Lista de produtos', 'Vender', 'Sair')
    print("----------------------------------------")
    opcao = int(input('Escolha uma opção e digite seu numero : '))
    
    if opcao == 1:
        nome = input("Qual o nome do produto ? ")
        preco = float(input("Qual o preço do produto ? "))
        quantidade = int(input("Qual a quantidade em estoque ? "))

        produto = [] # lista onde os produtos irao ficar armazenados enquanto o codigo estiver aberto

        produto.append(nome)
        produto.append(preco)
        produto.append(quantidade)
        produtos.append(produto)  

    if opcao == 2:
        print(listarprodutos()) 
    
    if opcao == 3:
        print("Escolha um produto a baixo:  ")
        listarprodutos()
        print("")
        numero = int(input("Informe o número do produto: "))
        print("")
        quantidade = int(input("Qual a quantidade?  "))

        if produtos[numero][2] >= quantidade: 
            print("----------------------------------------")
            print("")
            print("Produto vendido com sucesso!\n ==========* Nota Fiscal *========== \nInformações da venda:\n \nProduto: {}\nQuantidade: {}\nValor total da venda: R${:.2f}".format(produtos[numero][0], quantidade, quantidade*produtos[numero][1] ),"\n")
            produtos[numero][2] -= quantidade # Aqui vai ser chamado o numero do produto, o produto e a quantidades em estoque, por fim vai mostra a nota fiscal com as informações da venda 
        else:
            print("")
            print("Quantidade indisponível em estoque :")
                   
    if opcao == 4:
        print("")
        print("++++++++ fim do programa ++++++++")
        print("")
        break # responsavel por finalizar o loop 
