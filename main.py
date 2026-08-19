import mysql.connector

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="reciclagem"
        )

        return conexao
    
    except mysql.connector.Error as erro:
        print("Erro ao conectar ao MySQL:", erro)
        return None

from mysql import  *
from datetime import date

def validar_texto(texto, campo):
    texto = texto.strip()

    if texto == "":
        print(f"{campo} não pode ficar vazio.")
        return False

    if "  " in texto:
        print(f"{campo} não pode ter espaços duplicados.")
        return False

    return True


def validar_nome(nome, campo="Nome"):
    nome = nome.strip()

    if not validar_texto(nome, campo):
        return False

    if any(char.isdigit() for char in nome):
        print(f"{campo} não pode conter números.")
        return False

    if len(nome) < 3:
        print(f"{campo} deve ter pelo menos 3 caracteres.")
        return False

    return True


def validar_categoria(categoria):
    categoria = categoria.strip()

    if not validar_texto(categoria, "Categoria"):
        return False

    if any(char.isdigit() for char in categoria):
        print("Categoria não pode conter números.")
        return False

    return True


def validar_endereco(endereco):
    endereco = endereco.strip()

    if not validar_texto(endereco, "Endereço"):
        return False

    if len(endereco) < 5:
        print("Endereço muito curto.")
        return False

    return True

def cadastrar_material():
    print("\n--- CADASTRAR MATERIAL ---")

    nome = input("Nome do material: ")

    if not validar_nome(nome, "Nome do Material: "):
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
        INSERT INTO materiais (nome, categoria)
        VALUES (%s, %s)
        """,
        (nome, categoria)
    )

    conexao.commit()

    cursor.close()
    conexao.close()

    print("\nMaterial cadastrado com sucesso!")


def listar_materiais():

    conexao = conectar()

    if conexao is None:
        return []

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, categoria
        FROM materiais
        ORDER BY nome
    """)

    materiais = cursor.fetchall()

    cursor.close()
    conexao.close()

    return materiais


def mostrar_materiais():

    print("\n--- MATERIAIS ---")

    materiais = listar_materiais()

    if not materiais:
        print("Nenhum material cadastrado.")
        return

    for material in materiais:
        print(
            f"ID: {material[0]} | "
            f"Nome: {material[1]} | "
            f"Categoria: {material[2]}"
        )

def remover_Material():
    print("Remover material")

    listar_materiais()

    try:
        material_id = int(input("Digite o ID do material que deseja remover: "))
    except ValueError:
        print("ID Inválido")
        return
    conexao = conectar()

    if conexao is None:
        return

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT nome
        FROM materiais
        WHERE id = %s
    """, (material_id,))

    material = cursor.fetchone()

    if material is None:
        print("material não encontrado.")
        cursor.close()
        conexao.close()
        return

    cursor.execute("""
        SELECT COUNT(*)
        FROM coletas
        WHERE material_id = %s
    """, (material_id,))

    while True:

        quantidade_coletas = cursor.fetchone()[0]

        if quantidade_coletas > 0:
            print("\n Não é possivel remover este material.")
            print(f"Existem {quantidade_coletas} coletas registradas para este material.")
            cursor.close()
            conexao.close()
            return

        confirmar = input(f"\n deseja realmente remover o material {material[0]}? responda com: (s/n)")
        if confirmar.lower() == "s" or confirmar.lower() == "sim":
            cursor.execute("""
                DELETE FROM materiais
                WHERE id = %s
            """, (material_id,))

            conexao.commit()

            print("\nMaterial removido com sucesso!")
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

    materiais = listar_materiais()

    if not materiais:
        print("Cadastre um material primeiro.")
        return

    print("\nMateriais disponíveis:")

    for material in materiais:
        print(
            f"{material[0]} - "
            f"{material[1]} ({material[2]})"
        )

    try:
        material_id = int(input("\nID do material: "))
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
        (material_id, ponto_id, quantidade, data_coleta)
        VALUES (%s, %s, %s, %s)
        """,
        (
            material_id,
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
            m.nome,
            p.nome,
            c.quantidade,
            c.data_coleta
        FROM coletas c
        INNER JOIN materiais m
            ON c.material_id = m.id
        INNER JOIN pontos_coleta p
            ON c.ponto_id = p.id
        ORDER BY c.data_coleta DESC
    """)

    coletas = cursor.fetchall()

    if not coletas:
        print("Nenhuma coleta registrada.")

    for coleta in coletas:
        print("\nID:", coleta[0])
        print("Material:", coleta[1])
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

    print("\n--- TOTAL POR MATERIAL ---")

    cursor.execute("""
        SELECT
            m.nome,
            SUM(c.quantidade)
        FROM coletas c
        INNER JOIN materiais m
            ON c.material_id = m.id
        GROUP BY m.id, m.nome
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


def menu():

    while True:

        print("\n")
        print("=" * 45)
        print("       SISTEMA DE RECICLAGEM")
        print("=" * 45)

        print("1 - Cadastrar material")
        print("2 - Listar materiais")
        print("3 - Cadastrar ponto de coleta")
        print("4 - Listar pontos de coleta")
        print("5 - Registrar coleta")
        print("6 - Listar coletas")
        print("7 - Relatório")
        print("8 - Remover Material")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_material()

        elif opcao == "2":
            mostrar_materiais()

        elif opcao == "3":
            cadastrar_ponto()

        elif opcao == "4":
            mostrar_pontos()

        elif opcao == "5":
            registrar_coleta()

        elif opcao == "6":
            listar_coletas()

        elif opcao == "7":
            relatorio()

        elif opcao == "8":
            remover_Material()

        elif opcao == "0":
            print("\nSistema encerrado.")
            break

        else:
            print("\nOpção inválida.")


if __name__ == "__main__":
    menu()
    