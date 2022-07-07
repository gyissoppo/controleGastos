import mysql.connector
import conexaoBD #Classe que faz a conexão com o banco de dados
import operacoes




db_connection = conexaoBD.conectar()
con = db_connection.cursor()

def inserirMes(codigo, mesAno, ganho):
    try:
        sql = "insert into mes(codigo, mesAno, ganho) values('{}', '{}', '{}')".format(codigo, mesAno, ganho)
        con.execute(sql)
        db_connection.commit()#insercao de dados no banco de dados
        print("{} inserido!".format(con.rowcount))
    except Exception as erro:
        return erro

def inserirGastos(dia, periodo, item, valor, onde, forma):
    try:
        sql = "insert into gastos(codigo, dia, periodo, item, valor, onde, forma) values('', '{}', '{}', '{}', '{}', '{}', '{}')".format(dia, periodo, item, valor, onde, forma)
        con.execute(sql)
        db_connection.commit()#insercao de dados no banco de dados
        print("{} inserido!".format(con.rowcount))
    except Exception as erro:
        return erro


def consultarMes():
    try:
        sql = 'select * from mes'
        con.execute(sql)
        for (codigo, mesAno, ganho) in con:
                print('\nperíodo: {} \ncódigo: {} \nganho: {}'.format(mesAno, codigo, ganho))# \ntotal gasto no mês: {}\nsaldo restante do mês:
        print('\n')
    except Exception as erro:
        print(erro)

def consultarGastos(peri):
    try:
        sql = "select * from gastos where periodo = '{}'".format(peri)
        con.execute(sql)
        for (codigo, dia, periodo, item, valor, onde, forma) in con:
            print('\ncódigo: {} \ndata: {} \nperiodo: {} \nem que foi gasto: {} \nvalor do gatso:{} \nonde foi gasto:{} \nforma de pagamento: {}'.format(codigo, dia, periodo, item, valor, onde, forma))
        print('\n')
    except Exception as erro:
        print(erro)

def atualizarMes(cod, campo, novoDado):
    try:
        sql = "update mes set {} = '{}' where codigo = '{}'".format(campo, novoDado, cod)
        con.execute(sql)
        db_connection.commit()
        print('{} atualizado!'.format(con.rowcount))
    except Exception as erro:
        print(erro)

def atualizarGastos(cod, campo, novoDado):
    try:
        sql = "update gastos set {} = '{}' where codigo = '{}'".format(campo, novoDado, cod)
        con.execute(sql)
        db_connection.commit()
        print('{} atualizado!'.format(con.rowcount))
    except Exception as erro:
        print(erro)

def excluirMes(cod):
    try:
        sql = "delete from mes where codigo = '{}'".format(cod)
        con.execute(sql)
        db_connection.commit()
        print('{} excluído!'.format(con.rowcount))
    except Exception as erro:
        print(erro)

def excluirGastos(cod):
    try:
        sql = "delete from gastos where codigo = '{}'".format(cod)
        con.execute(sql)
        db_connection.commit()
        print('{} excluído!'.format(con.rowcount))
    except Exception as erro:
        print(erro)

def somarGastos(peri):
    try:
        sql = "SELECT SUM(valor) FROM gastos WHERE periodo = '{}'".format(peri)
        con.execute(sql)
        for (valor) in con:
            print('\nvalor total do gasto mensal:{}'.format(valor))
        print('\n')
    except Exception as erro:
        print(erro)

#def tratarData(texto):
    #separado = texto.split('/')
    #mes = separado[0]
    #ano = separado[1]
    #return '{}{}'.format(mes, ano)
#exemlpo de tratar: operacoes.atualizar(this.codigo, 'dataDeNascimento', operacoes.tratarData(this.campo))