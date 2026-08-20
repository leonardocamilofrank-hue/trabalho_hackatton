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
