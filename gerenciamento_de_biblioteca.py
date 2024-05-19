def adicionar_livro(biblioteca, titulo, autor):
    if titulo not in biblioteca:
        biblioteca[titulo] = {"autor": autor, "status": "disponível"}
        print(f'O livro "{titulo}" foi adicionado.')
    else:
        print(f'O livro "{titulo}" já existe na biblioteca.')

def remover_livro(biblioteca, titulo):
    if titulo in biblioteca:
        del biblioteca[titulo]
        print(f'O livro "{titulo}" foi removido.')
    else:
        print(f'O livro "{titulo}" não foi encontrado na biblioteca.')

def buscar_livro_por_titulo(biblioteca, titulo):
    if titulo in biblioteca:
        return biblioteca[titulo]
    else:
        print(f'O livro "{titulo}" não foi encontrado.')
        return None

def buscar_livro_por_autor(biblioteca, autor):
    livros_do_autor = [titulo for titulo, info in biblioteca.items() if info["autor"] == autor]
    if livros_do_autor:
        return livros_do_autor
    else:
        print(f'Nenhum livro do autor "{autor}" foi encontrado.')
        return []

def listar_livros(biblioteca):
    if biblioteca:
        for titulo, info in biblioteca.items():
            print(f'Título: {titulo}, Autor: {info["autor"]}, Status: {info["status"]}')
    else:
        print("A biblioteca está vazia.")


def main():
    biblioteca = {}
    while True:
        print("\nSistema de Gerenciamento de Biblioteca")
        print("1. Adicionar Livro")
        print("2. Remover Livro")
        print("3. Buscar Livro por Título")
        print("4. Buscar Livro por Autor")
        print("5. Listar Todos os Livros")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            adicionar_livro(biblioteca, titulo, autor)
        elif opcao == "2":
            titulo = input("Digite o título do livro a ser removido: ")
            remover_livro(biblioteca, titulo)
        elif opcao == "3":
            titulo = input("Digite o título do livro: ")
            livro = buscar_livro_por_titulo(biblioteca, titulo)
            if livro:
                print(f'Título: {titulo}, Autor: {livro["autor"]}, Status: {livro["status"]}')
        elif opcao == "4":
            autor = input("Digite o autor: ")
            livros = buscar_livro_por_autor(biblioteca, autor)
            for livro in livros:
                print(f'Título: {livro}')
        elif opcao == "5":
            listar_livros(biblioteca)
        elif opcao == "6":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
