import csv
import os
os.system ('cls')


def lerBancoDados():
    arquivo_csv = open('bancodedados.csv')
    leitor = csv.DictReader(arquivo_csv)
    dados = list(leitor)
    arquivo_csv.close()
    return dados



def escreverBancoDados(livros):
    arquivo_csv = open('bancodedados.csv', 'w', newline='')
    topicos = ['Nome', 'Autor', 'Categoria', 'Dinheiro_Gasto']
    escritor = csv.DictWriter(arquivo_csv, fieldnames=topicos)
    escritor.writeheader()
    escritor.writerows(livros)
    arquivo_csv.close()



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



def visualizarBiblioteca():
    livros = lerBancoDados()

    if not livros:
        print("Não há livros na biblioteca.")
    else:
        for livro in livros:
            print(f"{livro['Nome']} - {livro['Autor']} - {livro['Categoria']} - R${livro['Dinheiro_Gasto']}")
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



def visualizarCategoria():
    categoria = input("Digite a categoria para visualizar os livros: ")

    livros = lerBancoDados()
    livrosCategoria = [livro for livro in livros if livro['Categoria'] == categoria]

    if not livrosCategoria:
        print(f"Não há livros na categoria '{categoria}'.")
    else:
        for livro in livrosCategoria:
            print(f"{livro['Nome']} - {livro['Autor']} - R${livro['Dinheiro_Gasto']}")


