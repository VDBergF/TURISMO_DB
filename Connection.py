# coding=utf-8
import json
import psycopg2

class Connection():
    input_city = json.loads(open("./Data/cidades.txt").read())  # Json

    def __init__(self):
        self.con = psycopg2.connect(host='localhost', port='5432', database='TURISMO_DB', user='postgres', password='041097')
        self.cur = self.con.cursor()

    # def insert_data_in_city(self):
    #     for i in self.input_city:
    #         self.cur.execute("INSERT INTO cidade VALUES (%s, '%s', '%s', %d)" % ('default', i['nome'], i['estado'], i['populacao']))
    #
    #     self.con.commit()

    def insert_data_in_city(self):
        file = open('./Data/cidades2.txt', 'r')
        for i in file:
            nome, estado, populacao = i.split('|')
            self.cur.execute("INSERT INTO cidade VALUES (%s, '%s', '%s', %d)" % ('default', nome, estado, int(populacao)))
        self.con.commit()

    def insert_data_in_casa_show(self):
        file = open('./Data/casa_show.txt', 'r')
        for i in file:
            horario_inicio, dia_fecha, descricao = i.split('|')
            self.cur.execute("INSERT INTO casa_show VALUES (%s, '%s', '%s', '%s')" % ('default', horario_inicio, dia_fecha, descricao))
        self.con.commit()

    def insert_data_in_fundador(self):
        file = open('./Data/fundadores.txt', 'r')
        for i in file:
            data_nascimento, data_morte, nacionalidade, profissao, nome = i.split('|')
            self.cur.execute("INSERT INTO fundador VALUES (%s, '%s', '%s', '%s', '%s', %d)" % ('default', data_nascimento, data_morte,
                                                                                      nacionalidade, profissao, nome))
        self.con.commit()


c = Connection()
c.insert_data_in_fundador()