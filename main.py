import mysql.connector
from menu import *

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


if __name__ == "__main__":
    menu()