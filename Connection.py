# coding=utf-8
import psycopg2
import random

class Connection():
    lstCity = None
    lstCasaShow = None
    lstRestaurante = None
    lstHotel = None
    lstMuseu = None
    lstFundador = None

    def __init__(self):
        self.con = psycopg2.connect(host='localhost', port='5432', database='TURISMO_DB', user='postgres', password='041097')
        self.cur = self.con.cursor()

    def insert_data_in_city(self):
        file = open('./Data/cidades.txt', 'r')
        for i in file:
            nome, estado, populacao = i.split('|')
            self.cur.execute("INSERT INTO cidade VALUES (%s, '%s', '%s', %d)" % ('default', nome, estado, int(populacao)))
        self.con.commit()

    def select_data_in_city(self):
        self.cur.execute('SELECT codigo FROM cidade')
        codigos = [data[0] for data in self.cur.fetchall()]
        return codigos

    def insert_data_in_casa_show(self):
        file = open('./Data/casa_show.txt', 'r')
        if (self.lstCity == None): self.lstCity = self.select_data_in_city()
        if (self.lstRestaurante == None): self.lstRestaurante = self.select_data_in_restaurante()

        j = 0
        for i in file:
            nome, rua, bairro, numero, descricao, horario_inicio, dia_fecha = i.split('|')
            if j % 2 == 0:
                self.cur.execute("INSERT INTO casa_show VALUES "
                                 "(%s, '%s', '%s', '%s', '%s', '%s', %d, '%s', %d, %d)" % ('default', nome, rua, bairro, numero,
                                  descricao,  int(horario_inicio), dia_fecha, random.choice(self.lstCity), random.choice(self.lstRestaurante)))
            else:
                self.cur.execute("INSERT INTO casa_show VALUES "
                                 "(%s, '%s', '%s', '%s', '%s', '%s', %d, '%s', %d)" % ('default', nome, rua, bairro, numero,
                                  descricao, int(horario_inicio), dia_fecha, random.choice(self.lstCity)))

            j = j+1
        self.con.commit()

    def select_data_in_casa_show(self):
        self.cur.execute('SELECT codigo FROM casa_show')
        codigos = [data[0] for data in self.cur.fetchall()]
        return codigos

    def insert_data_in_fundador(self):
        file = open('./Data/fundadores.txt', 'r')
        for i in file:
            data_nascimento, data_morte, nacionalidade, profissao, nome = i.split('|')
            self.cur.execute("INSERT INTO fundador VALUES (%s, '%s', '%s', '%s', '%s', '%s')" % ('default', data_nascimento, data_morte,
                                                                                      nacionalidade, profissao, nome))
        self.con.commit()

    def select_data_in_fundador(self):
        self.cur.execute('SELECT codigo FROM fundador')
        codigos = [data[0] for data in self.cur.fetchall()]
        return codigos

    def insert_data_in_hotel(self):
        file = open('./Data/hoteis.txt', 'r')
        if (self.lstCity == None): self.lstCity = self.select_data_in_city()
        if (self.lstRestaurante == None): self.lstRestaurante = self.select_data_in_restaurante()

        j = 0
        for i in file:
            nome, rua, bairro, numero, tipo = i.split('|')
            if j % 2 == 0:
                self.cur.execute("INSERT INTO hotel VALUES "
                                 "(%s, '%s', '%s', '%s', '%s', %d, %d, %d)" % ('default', nome, rua, bairro, numero,
                                  random.choice(self.lstCity), int(tipo), random.choice(self.lstRestaurante)))
            else:
                self.cur.execute("INSERT INTO hotel VALUES "
                                 "(%s, '%s', '%s', '%s', '%s', %d, %d)" % ('default', nome, rua, bairro, numero,
                                  random.choice(self.lstCity), int(tipo)))

            j = j+1
        self.con.commit()

    def select_data_in_hotel(self):
        self.cur.execute('SELECT codigo FROM hotel')
        codigos = [data[0] for data in self.cur.fetchall()]
        return codigos

    def insert_data_in_igreja(self):
        file = open('./Data/igrejas.txt', 'r')
        if (self.lstCity == None): self.lstCity = self.select_data_in_city()

        for i in file:
            nome, rua, bairro, numero, descricao, estilo, data_construcao = i.split('|')
            self.cur.execute("INSERT INTO igreja VALUES (%s, '%s', '%s', '%s', '%s', '%s', '%s', '%s', %d)" % ('default', nome, rua, bairro,
                             numero, descricao, estilo, data_construcao, random.choice(self.lstCity)))
        self.con.commit()

    def insert_data_in_museu(self):
        file = open('./Data/museus.txt', 'r')
        if (self.lstCity == None): self.lstCity = self.select_data_in_city()
        for i in file:
            nome, rua, bairro, numero, descricao, n_salas = i.split('|')
            self.cur.execute("INSERT INTO museu VALUES (%s, '%s', '%s', '%s', '%s', '%s', %d, %d)" % ('default', nome, rua, bairro,
                                                                                            numero, descricao, int(n_salas), random.choice(self.lstCity)))
        self.con.commit()

    def select_data_in_museu(self):
        self.cur.execute('SELECT codigo FROM museu')
        codigos = [data[0] for data in self.cur.fetchall()]
        return codigos

    def insert_data_in_restaurante(self):
        file = open('./Data/restaurantes.txt', 'r')
        if (self.lstCity == None): self.lstCity = self.select_data_in_city()

        for i in file:
            nome, rua, bairro, numero, especialidade, preco_medio, tipo = i.split('|')
            self.cur.execute("INSERT INTO restaurante VALUES (%s, '%s', '%s', '%s', '%s', '%s', '%s', '%s', %d)" % ('default', nome, rua, bairro,
                                                                                                  numero, especialidade,
                                                                                                  preco_medio, tipo,
                                                                                                  random.choice(self.lstCity)))
        self.con.commit()

    def select_data_in_restaurante(self):
        self.cur.execute('SELECT codigo FROM restaurante')
        codigos = [data[0] for data in self.cur.fetchall()]
        return codigos

    def insert_data_in_quarto(self):
        file = open('./Data/quartos.txt', 'r')
        if (self.lstHotel == None): self.lstHotel = self.select_data_in_hotel()

        j = 0
        for i in file:
            preco, tipo = i.split('|')
            codigo_hotel = random.choice(self.lstHotel)
            self.cur.execute("INSERT INTO quarto VALUES (%d, '%s', %s, %d)" % (float(preco), tipo, 'default', codigo_hotel))

        self.con.commit()

    def insert_data_in_fundacoes(self):
        file = open('./Data/fundacoes.txt', 'r')
        if (self.lstMuseu == None): self.lstMuseu = self.select_data_in_museu()
        if (self.lstFundador == None): self.lstFundador = self.select_data_in_fundador()

        for i in file:
            data = str(i)
            self.cur.execute("INSERT INTO funda VALUES (%d, %d, '%s')" % (random.choice(self.lstFundador),
                                                                              random.choice(self.lstMuseu), data))
        self.con.commit()

c = Connection()
#c.insert_data_in_city()
#c.insert_data_in_restaurante()
#c.insert_data_in_casa_show()
#c.insert_data_in_hotel()
c.insert_data_in_quarto()
#c.insert_data_in_igreja()
#c.insert_data_in_museu()
#c.insert_data_in_fundador()
#c.insert_data_in_fundacoes()