# Lista que guardará vários dicionários (produtos)
produtos = []

print("=== Sistema de Cadastro de Produtos ===")

while True:
    print("\nEscolha uma opção:")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto por nome")
    print("4 - Sair")

    opcao = input("Opção: ")

    # Estrutura condicional
    if opcao == "1":
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))

        # Dicionário representando um produto
        produto = {
            "nome": nome,
            "preco": preco
    }

        # Adiciona o produto à lista
        produtos.append(produto)
        print("Produto cadastrado com sucesso!")

    elif opcao == "2":
        print("\n=== Lista de Produtos ===")

        # Estrutura de repetição para exibir todos os produtos
        if len(produtos) == 0:
            print("Nenhum produto cadastrado.")
        else:
            for p in produtos:
                print(f"Nome: {p['nome']} | Preço: R$ {p['preco']:.2f}")

    elif opcao == "3":
        busca = input("Digite o nome do produto para buscar: ")
        encontrado = False

        for p in produtos:  # loop para buscar
            if p["nome"].lower() == busca.lower():
                print(f"Produto encontrado! Preço: R$ {p['preco']:.2f}")
                encontrado = True
                break
        
        if not encontrado:
            print("Produto não encontrado.")

    elif opcao == "4":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida! Tente novamente.")

