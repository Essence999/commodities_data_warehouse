import os

# Diretórios a serem excluídos
EXCLUDED_DIRS = {'.venv', 'target', 'logs', '.git'}


def print_directory_tree(path, indent=0):
    """
    Imprime a estrutura de diretórios e arquivos a partir do caminho fornecido,
    excluindo diretórios especificados.

    :param path: Caminho do diretório para listar a estrutura.
    :param indent: Nível de indentação atual (para efeitos de recuo na árvore).
    """
    if not os.path.isdir(path):
        print(f"'{path}' não é um diretório válido.")
        return

    # Listar todos os itens no diretório
    items = os.listdir(path)
    items.sort()

    for item in items:
        if item in EXCLUDED_DIRS:
            continue

        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            # Se o item é um diretório, imprimir e chamar a função recursivamente
            print('    ' * indent + '├── ' + item)
            print_directory_tree(item_path, indent + 1)
        else:
            # Se o item é um arquivo, imprimir com indentação
            print('    ' * indent + '└── ' + item)


# Exemplo de uso
if __name__ == "__main__":
    directory_path = input("Digite o caminho do diretório: ")
    print_directory_tree(directory_path)
