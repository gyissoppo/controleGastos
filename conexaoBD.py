import mysql.connector #faz acesso ao mysql
from mysql.connector import errorcode #trata as excecoes que vao surgir

def conectar():
    try:
        db_connection = mysql.connector.connect(host='localhost',
                                                user='root',
                                                password='',
                                                database='tabelagastos')
        print('conectado com sucesso!')
        return db_connection
    except mysql.connector.Error as erro: #guardando as possiveis excecoes na variavel erro
        if erro.errno == errorcode.ER_BAD_DB_ERROR: #caso o banco de dados nao exista
            print('banco de dados nao existe!, {}'.format(erro))
        elif erro.errno == errorcode.ER_ACESS_DENIED_ERROR: #caso usuario ou senha estejam incorretos
            print('usuario ou senha nao sao validos!, {}'.format(erro))
        else:
            print(erro)
    else:
        db_connection.close()