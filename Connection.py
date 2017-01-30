# coding=utf-8
import psycopg2

class Connection():

    def __init__(self):
        self.con = psycopg2.connect(host='localhost', port='5432', database='TURISMO_DB', user='postgres', password='041097')
        self.cur = self.con.cursor()

    def insert_data_in_city(self):
        file = open('./Data/cidades.txt', 'r')
        for i in file:
            nome, estado, populacao = i.split('|')
            self.cur.execute("INSERT INTO cidade VALUES (%s, '%s', '%s', %d)" % ('default', nome, estado, int(populacao)))
        self.con.commit()

    def insert_data_in_casa_show(self):
        file = open('./Data/casa_show.txt', 'r')
        for i in file:
            horario_inicio, dia_fecha, descricao, nome, endereco = i.split('|')
            self.cur.execute("INSERT INTO casa_show VALUES (%s, '%s', '%s', '%s', '%s', %d)" % ('default', dia_fecha,
                                                                                                descricao, nome, endereco,
                                                                                                int(horario_inicio)))
        self.con.commit()

    def insert_data_in_fundador(self):
        file = open('./Data/fundadores.txt', 'r')
        for i in file:
            data_nascimento, data_morte, nacionalidade, profissao, nome = i.split('|')
            self.cur.execute("INSERT INTO fundador VALUES (%s, '%s', '%s', '%s', '%s', %s)" % ('default', data_nascimento, data_morte,
                                                                                      nacionalidade, profissao, nome))
        self.con.commit()

    def insert_data_in_hotel(self):
        file = open('./Data/hoteis.txt', 'r')
        for i in file:
            tipo, nome, endereco = i.split('|')
            self.cur.execute("INSERT INTO hotel VALUES (%s, '%s', '%s', '%s')" % ('default', tipo, nome, endereco))
        self.con.commit()

    def insert_data_in_igreja(self):
        file = open('./Data/igrejas.txt', 'r')
        for i in file:
            estilo, data_construcao, descricao, nome, endereco = i.split('|')
            self.cur.execute("INSERT INTO igreja VALUES (%s, '%s', '%s', '%s', '%s', '%s')" % ('default', estilo,
                                                                                                data_construcao, descricao,
                                                                                                nome, endereco))
        self.con.commit()

    def insert_data_in_museu(self):
        file = open('./Data/museus.txt', 'r')
        for i in file:
            n_salas, descricao, data_fundacao, endereco, nome = i.split('|')
            self.cur.execute("INSERT INTO museu VALUES (%s, '%s', '%s', '%s', '%s', %d)" % ('default', descricao, data_fundacao,
                                                                                            endereco, nome, int(n_salas)))
        self.con.commit()

    def insert_data_in_restaurante(self):
        file = open('./Data/museus.txt', 'r')
        for i in file:
            especialidade, preco_medio, tipo, nome, endereco = i.split('|')
            self.cur.execute("INSERT INTO restaurante VALUES (%s, %s, '%d', '%s', '%s', '%s')" % ('default', especialidade,
                                                                                                preco_medio, tipo,
                                                                                                nome, endereco))
        self.con.commit()

    def insert_data_in_quarto(self):
        file = open('./Data/quartos.txt', 'r')
        for i in file:
            preco, tipo = i.split('|')
            self.cur.execute("INSERT INTO quarto VALUES (%s, %d, '%s', '%s', '%s', '%s')" % ('default', preco, tipo))
        self.con.commit()

c = Connection()
c.insert_data_in_museu()