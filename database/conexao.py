import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host="localhost:3306",
        user="root",
        password="root",
        database="coleta_seletiva"

    )
    return conexao
    
