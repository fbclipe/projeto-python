import csv
import os
os.system ('cls')

# Função para leitura dos dados no arquivo csv
def lerBancoDados():
    arquivo_csv = open('bancodedados.csv', 'r')
    leitor = csv.DictReader(arquivo_csv)
    dados = list(leitor)
    arquivo_csv.close()
    return dados


# Função para escrever dados no arquivo csv
def escreverBancoDados(livros):
    arquivo_csv = open('bancodedados.csv', 'w', newline='')
    topicos = ['Nome', 'Autor', 'Categoria', 'Dinheiro_Gasto']
    escritor = csv.DictWriter(arquivo_csv, fieldnames=topicos)
    escritor.writeheader()
    escritor.writerows(livros)
    arquivo_csv.close()


# Função para adição de livros
def adicionar():
    nome = input("Nome do livro: ")
    autor = input("Autor: ")
    categoria = input("Categoria: ")
    try:
        dinheiroGasto = float(input("Digite o valor gasto no livro: "))
    except(ValueError):
        dinheiroGasto = float(input("Valor inválido. Tente novamente: "))

    novoLivro = {'Nome': nome, 'Autor': autor, 'Categoria': categoria, 'Dinheiro_Gasto': dinheiroGasto}

    livros = lerBancoDados()
    livros.append(novoLivro)
    escreverBancoDados(livros)

    print("Livro adicionado!")


# Função para visualização da biblioteca
def visualizarBiblioteca():
    livros = lerBancoDados()

    if not livros:
        print("Não há livros na biblioteca!")
    else:
        for livro in livros:
            print(f"{livro['Nome']} - {livro['Autor']} - {livro['Categoria']} - R${livro['Dinheiro_Gasto']}")


# Função para atualizar dados dos livros dentro da biblioteca
def atualizar():
    nomeLivro = input("Digite livro que você deseja atualizar: ")

    livros = lerBancoDados()
    livroEncontrado = False

    for livro in livros:
        if livro['Nome'] == nomeLivro:
            livroEncontrado = True
            print("Encontrado:")
            print(f"{livro['Nome']} - {livro['Autor']} - {livro['Categoria']} - R${livro['Dinheiro_Gasto']}")
            print("\n- Nome","\n- Autor","\n- Categoria","\n- Preço","\n- Tudo")
            decisao = input("\nEscreva o que deseja alterar: \n")
            if decisao.lower().strip() == "nome":
                livro['Nome'] = input("Digite um novo nome para o livro: ")
            elif decisao.lower().strip() == "autor":
                livro['Autor'] = input("Digite um novo autor: ")
            elif decisao.lower().strip() == "categoria":
                livro['Categoria'] = input("Digite a categoria nova: ")
            elif decisao.lower().strip() == "preço":
                try:
                    livro['Dinheiro_Gasto'] = float(input("Digite o novo valor gasto: "))
                except (ValueError):
                    livro['Dinheiro_Gasto'] = float(input("Valor inválido. Tente novamente: "))
            elif decisao.lower().strip() == "tudo":
                livro['Nome'] = input("Digite um novo nove para o livro: ")
                livro['Autor'] = input("Digite um novo autor: ")
                livro['Categoria'] = input("Digite a categoria nova: ")
                try:
                    livro['Dinheiro_Gasto'] = float(input("Digite o novo valor gasto: "))
                except (ValueError):
                    livro['Dinheiro_Gasto'] = float(input("Valor invalido. Tente novamente: "))

            escreverBancoDados(livros)
            print("Livro atualizado!")

    if not livroEncontrado:
        print(f"Você não possui'{nomeLivro}' na sua biblioteca.")


# Função para excluir livros da biblioteca
def excluir():
    nomeLivro = input("Digite o livro que deseja excluir: ")

    livros = lerBancoDados()
    livroEncontrado = False

    for livro in livros:
        if livro['Nome'] == nomeLivro:
            livroEncontrado = True
            livros.remove(livro)
            escreverBancoDados(livros)
            print("Livro excluído!")

    if not livroEncontrado:
        print(f"O livro '{nomeLivro}' não foi encontrado na biblioteca.")


# Função para visualizar livros de acordo com a categoria escolhida
def visualizarCategoria():
    categoria = input("Digite a categoria para visualizar os livros: ")

    livros = lerBancoDados()
    livrosCategoria = [livro for livro in livros if livro['Categoria'] == categoria]

    if not livrosCategoria:
        print(f"Não há livros na categoria '{categoria}'.")
    else:
        for livro in livrosCategoria:
            print(f"{livro['Nome']} - {livro['Autor']} - R${livro['Dinheiro_Gasto']}")


# Função para separar os livros de acordo com as categorias
def extratoCategoria():
    livros = lerBancoDados()
    
    categorias = []
    
    for livro in livros:
        categoria = livro['Categoria']
        if categoria not in categorias:
            categorias.append(categoria)
        
    for categoria in categorias:
          
        livrosCategoria = [livro for livro in livros if livro['Categoria'] == categoria]
        totalGastosCategoria = sum(float(livro['Dinheiro_Gasto']) for livro in livrosCategoria)

        print(f"=== Categoria: {categoria} ===")
        for livro in livrosCategoria:
            print(f"{livro['Nome']} - R${livro['Dinheiro_Gasto']}")
            
        print(f"Total gasto na categoria {categoria}: R${totalGastosCategoria:.2f}")
        print()


# Função para mostrar os gastos totais com a biblioteca
def gastosTotais():
    livros = lerBancoDados()
    totalGastos = sum(float(livro['Dinheiro_Gasto']) for livro in livros)

    print(f"Valor total gasto na coleção: R${totalGastos:.2f}")


# Função para mostrar a média de gastos
def mediaGastos():
    livros = lerBancoDados()
    try:
        mediaGastos = sum(float(livro['Dinheiro_Gasto']) for livro in livros)/len(livros)
        print(f"A média de gastos é de R${mediaGastos}")
    except ZeroDivisionError:
        print("Não é possível calcular a média de gastos pois não há livros na biblioteca")



while True:
    os.system("cls")

    print("===Gerenciamento da Biblioteca=== \n")
    print("1. Adicionar")
    print("2. Biblioteca")
    print("3. Atualizar Biblioteca")
    print("4. Excluir")
    print("5. Visualizar Categorias")
    print("6. Extrato por Categoria")
    print("7. Gastos Totais")
    print("8. Media de Gastos")
    print("0. Sair")

    opcao = input("Escolha uma função: ")

    if opcao == '1':
        adicionar()
    elif opcao == '2':
        visualizarBiblioteca()
    elif opcao == '3':
        atualizar()
    elif opcao == '4':
        excluir()
    elif opcao == '5':
        visualizarCategoria()
    elif opcao == '6':
        extratoCategoria()
    elif opcao == '7':
        gastosTotais()
    elif opcao == '8':
        mediaGastos()
    elif opcao == '0':
        break
    else:
        print("Valor incorreto, Tente novamente.")
    input("Pressione [Enter] para continuar...")
