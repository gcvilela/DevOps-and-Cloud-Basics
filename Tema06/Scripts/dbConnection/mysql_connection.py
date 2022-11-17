import mysql.connector

class connector_mysql():
    host = "<HOST>"
    user = "<USER>"
    password= "<PASSWORD>"
    database = "<DATABASE>"
    
    def connect(self):
        db_connection = mysql.connector.connect(host=self.host, user=self.user, passwd=self.password,
                                                database=self.database)
        cursor = db_connection.cursor()
        return db_connection,cursor
    
    def desconect(self,db_connection,cursor):
        cursor.close()
        db_connection.commit()
        db_connection.close()
    
    def insert_names(self,lista):
        db_connection, cursor = self.connect()
        for i in lista:
            query = "INSERT INTO actorsnames(nconst,qtdMovies,name) VALUES('{}',{},'{}')".format(i[0], i[1], i[2])
            cursor.execute(query)
        self.desconect(db_connection,cursor)
        print("Migração completa!")
    
    def get_names(self):
        db_connection, cursor = self.connect()
        query = "SELECT * FROM actorsnames"
        cursor.execute(query)
        linhas = cursor.fetchall()
        lista = []
        for linha in linhas:
            lista.append(linha[2])
        self.desconect(db_connection,cursor)
        print("Nomes salvos na lista!")
        return lista
    

    