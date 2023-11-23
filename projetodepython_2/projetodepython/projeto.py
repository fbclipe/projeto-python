import csv
import os
os.system ('cls')

# Função p/ leitura do banco de dados (arquivo .csv)
def lerBancoDados():
    with open('bancodedados.csv', 'r') as arquivo_csv: 
        leitor = csv.DictReader(arquivo_csv)
        return list(leitor)

# Função p/ atribuir itens ao banco de dados (arquivo .csv)
def escreverBancoDados(livros):
    with open('bancodedados.csv', 'w', newline='') as arquivo_csv:
        topicos = ['Nome', 'Autor', 'Categoria', 'Dinheiro_Gasto']
        escritor = csv.DictWriter(arquivo_csv, fieldnames=topicos)
        escritor.writeheader()
        escritor.writerows(livros)

# Função p/ adicionar itens na biblioteca
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

# Função p/ visualizar os itens contidos na biblioteca (banco de dados/ arquivo .csv)
def visualizarBiblioteca():
    livros = lerBancoDados()

    if not livros:
        print("Não há livros na biblioteca.")
    else:
        for livro in livros:
            print(f"{livro['Nome']} - {livro['Autor']} - {livro['Categoria']} - R${livro['Dinheiro_Gasto']}")

# Função p/ alterar valores dos itens contidos na biblioteca (banco de dados/ arquivo .csv)
def atualizar():
    nomeLivro = input("Digite livro que você quer atualizar: ")

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
                    livro['Dinheiro_Gasto'] = float(input("Valor inválido. Tente novamente: "))

            escreverBancoDados(livros)
            print("Livro atualizado!")

    if not livroEncontrado:
        print(f"Você não possui'{nomeLivro}' na sua biblioteca.")

# Função para excluir itens da biblioteca
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

# Funçaõ para visualizar os itens separadamente pelas categorias dos livros na biblioteca
def visualizarCategoria():
    categoria = input("Digite a categoria para visualizar os livros: ")

    livros = lerBancoDados()
    livrosCategoria = [livro for livro in livros if livro['Categoria'] == categoria]

    if not livrosCategoria:
        print(f"Não há livros na categoria '{categoria}'.")
    else:
        for livro in livrosCategoria:
            print(f"{livro['Nome']} - {livro['Autor']} - R${livro['Dinheiro_Gasto']}")

# Função que permite ver todos os itens pertencentes a cada categoria e as características de cada um
def extratoCategoria():
    livros = lerBancoDados()
    
    categorias = set(livro['Categoria'] for livro in livros)

    for categoria in categorias:
        
        livrosCategoria = [livro for livro in livros if livro['Categoria'] == categoria]
        
        totalGastosCategoria = sum(float(livro['Dinheiro_Gasto']) for livro in livrosCategoria)

        print(f"=== Categoria: {categoria} ===")
        for livro in livrosCategoria:
            print(f"{livro['Nome']} - R${livro['Dinheiro_Gasto']}")
        
        print(f"Total gasto na categoria {categoria}: R${totalGastosCategoria:.2f}")
        print()

# Função que mostra quanto foi gasto na aquisição de cada item contido na biblioteca pessoal
def gastosTotais():
    livros = lerBancoDados()
    totalGastos = sum(float(livro['Dinheiro_Gasto']) for livro in livros)

    print(f"Total de dinheiro gasto na coleção: R${totalGastos:.2f}")

# Função que mostra a média dos gastos ao comparar o preço total pago na aquisição dos itens com a quantidade de itens obtidos
def mediaGastos():
    livros = lerBancoDados()
    mediaGastos = sum(float(livro['Dinheiro_Gasto']) for livro in livros)/len(livros)
    print(f"A média de gastos é de R${mediaGastos}")


# Menu de opções de interação com a biblioteca
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
    print("8. Média de Gastos")
    print("0. Sair")

    escolha = input("Escolha uma função: ")

# O código abaixo representa as consequências e ações que o programa vai tomar de acordo com o valor que for escolhido (1, 2, 3, 4, 5, 6, 7, 8, 0)
    if escolha == '1':
        adicionar()
    elif escolha == '2':
        visualizarBiblioteca()
    elif escolha == '3':
        atualizar()
    elif escolha == '4':
        excluir()
    elif escolha == '5':
        visualizarCategoria()
    elif escolha == '6':
        extratoCategoria()
    elif escolha == '7':
        gastosTotais()
    elif escolha == '8':
        mediaGastos()
    elif escolha == '0':
        break
    else:
        print("Valor incorreto, Tente novamente.")
    
    input("Pressione Enter para continuar...")
