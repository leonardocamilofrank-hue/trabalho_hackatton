from main import conectar
from validacoes import *
from datetime import date

def cadastrar_itens():
    print("\n--- CADASTRAR ITEM ---")

    nome = input("Nome do item: ")

    if not validar_nome(nome, "Nome do item: "):
        return
    
    categoria = input("Categoria: ")

    if not validar_categoria(categoria):
        return

    conexao = conectar()

    if conexao is None:
        return

    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO itens (nome, categoria)
        VALUES (%s, %s)
        """,
        (nome, categoria)
    )

    conexao.commit()

    cursor.close()
    conexao.close()

    print("\nItem cadastrado com sucesso!")

def listar_itens():

    conexao = conectar()

    if conexao is None:
        return []

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, categoria
        FROM itens
        ORDER BY nome
    """)

    itens = cursor.fetchall()

    cursor.close()
    conexao.close()

    return itens

def mostrar_itens():

    print("\n--- ITENS ---")

    itens = listar_itens()

    if not itens:
        print("Nenhum material cadastrado.")
        return

    for item in itens:
        print(
            f"ID: {item[0]} | "
            f"Nome: {item[1]} | "
            f"Categoria: {item[2]}"
        )

def remover_item():
    print("Remover item")

    listar_itens()

    try:
        item_id = int(input("Digite o ID do item que deseja remover: "))
    except ValueError:
        print("ID Inválido")
        return
    conexao = conectar()

    if conexao is None:
        return

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT nome
        FROM itens
        WHERE id = %s
    """, (item_id,))

    item = cursor.fetchone()

    if item is None:
        print("item não encontrado.")
        cursor.close()
        conexao.close()
        return

    cursor.execute("""
        SELECT COUNT(*)
        FROM coletas
        WHERE item_id = %s
    """, (item_id,))

    while True:

        quantidade_coletas = cursor.fetchone()[0]

        if quantidade_coletas > 0:
            print("\n Não é possivel remover este item.")
            print(f"Existem {quantidade_coletas} coletas registradas para este item.")
            cursor.close()
            conexao.close()
            return

        confirmar = input(f"\n deseja realmente remover o item {item[0]}? responda com: (s/n)")
        if confirmar.lower() == "s" or confirmar.lower() == "sim":
            cursor.execute("""
                DELETE FROM itens
                WHERE id = %s
            """, (item_id,))

            conexao.commit()

            print("\nitem removido com sucesso!")
            return

        elif confirmar.lower() == "n" or confirmar.lower() == "nao" or confirmar.lower() == "não":
            print("\n Remoção Cancelada.")
            cursor.close()
            conexao.close()
            return

        else:
            print("Opção inválida. Responda com (s/n)")
            continue

def cadastrar_ponto():
    print("\n--- CADASTRAR PONTO DE COLETA ---")

    nome = input("Nome do ponto: ")

    if not validar_nome(nome, "Nome do ponto: "):
        return
    
    endereco = input("Endereço: ")

    if not validar_endereco(endereco):
        return

    conexao = conectar()

    if conexao is None:
        return

    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO pontos_coleta (nome, endereco)
        VALUES (%s, %s)
        """,
        (nome, endereco)
    )

    conexao.commit()

    cursor.close()
    conexao.close()

    print("\nPonto de coleta cadastrado com sucesso!")

def listar_pontos():

    conexao = conectar()

    if conexao is None:
        return []

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, endereco
        FROM pontos_coleta
        ORDER BY nome
    """)

    pontos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return pontos

def mostrar_pontos():

    print("\n--- PONTOS DE COLETA ---")

    pontos = listar_pontos()

    if not pontos:
        print("Nenhum ponto cadastrado.")
        return

    for ponto in pontos:
        print(
            f"ID: {ponto[0]} | "
            f"Nome: {ponto[1]} | "
            f"Endereço: {ponto[2]}"
        )

def registrar_coleta():

    print("\n--- REGISTRAR COLETA ---")

    itens = listar_itens()

    if not itens:
        print("Cadastre um item primeiro.")
        return

    print("\nItens disponíveis:")

    for item in itens:
        print(
            f"{item[0]} - "
            f"{item[1]} ({item[2]})"
        )

    try:
        item_id = int(input("\nID do item: "))
    except ValueError:
        print("ID inválido.")
        return

    pontos = listar_pontos()

    if not pontos:
        print("Cadastre um ponto de coleta primeiro.")
        return

    print("\nPontos disponíveis:")

    for ponto in pontos:
        print(
            f"{ponto[0]} - "
            f"{ponto[1]} - "
            f"{ponto[2]}"
        )

    try:
        ponto_id = int(input("\nID do ponto de coleta: "))
        quantidade = float(
            input("Quantidade coletada (kg): ")
        )
    except ValueError:
        print("Valor inválido.")
        return

    if quantidade <= 0:
        print("A quantidade deve ser maior que zero.")
        return

    conexao = conectar()

    if conexao is None:
        return

    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO coletas
        (item_id, ponto_id, quantidade, data_coleta)
        VALUES (%s, %s, %s, %s)
        """,
        (
            item_id,
            ponto_id,
            quantidade,
            date.today()
        )
    )

    conexao.commit()

    cursor.close()
    conexao.close()

    print("\nColeta registrada com sucesso!")

def listar_coletas():

    print("\n--- COLETAS REGISTRADAS ---")

    conexao = conectar()

    if conexao is None:
        return

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            c.id,
            i.nome,
            p.nome,
            c.quantidade,
            c.data_coleta
        FROM coletas c
        INNER JOIN itens i
            ON c.item_id = i.id
        INNER JOIN pontos_coleta p
            ON c.ponto_id = p.id
        ORDER BY c.data_coleta DESC
    """)

    coletas = cursor.fetchall()

    if not coletas:
        print("Nenhuma coleta registrada.")

    for coleta in coletas:
        print("\nID:", coleta[0])
        print("Item:", coleta[1])
        print("Ponto:", coleta[2])
        print("Quantidade:", coleta[3], "kg")
        print("Data:", coleta[4])
        print("-" * 40)

    cursor.close()
    conexao.close()

def relatorio():

    print("\n--- RELATÓRIO ---")

    conexao = conectar()

    if conexao is None:
        return

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT COALESCE(SUM(quantidade), 0)
        FROM coletas
    """)

    total = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM coletas
    """)

    quantidade_coletas = cursor.fetchone()[0]

    print("\nTotal reciclado:", total, "kg")
    print("Total de coletas:", quantidade_coletas)

    print("\n--- TOTAL POR ITEM ---")

    cursor.execute("""
        SELECT
            i.nome,
            SUM(c.quantidade)
        FROM coletas c
        INNER JOIN itens i
            ON c.item_id = i.id
        GROUP BY i.id, i.nome
        ORDER BY SUM(c.quantidade) DESC
    """)

    resultados = cursor.fetchall()

    for resultado in resultados:
        print(
            resultado[0],
            ":",
            resultado[1],
            "kg"
        )

    cursor.close()
    conexao.close()
