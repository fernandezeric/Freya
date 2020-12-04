#LEER
#https://www.freecodecamp.org/news/connect-python-with-sql/
#https://stackoverflow.com/questions/38076220/python-mysqldb-connection-in-a-class
"""
BUILDING PROCESS
"""
"""
Example for connect data base postgreSQL using psycopg2
"""
import psycopg2

class Connect_NAME ():

    def __init__(self,user,password,host,port,database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        #connect with data base
        self.connection_ = psycopg2.connect(user = self.user,
                                      password = self.password,
                                      host = self.host,
                                      port = self.port,
                                      database = self.database)
        
        self.cursor_ = self.connection_.cursor()

    def __enter__(self):
        return self

    def __exit__(self,exc_type,exc_val,exc_tb):
        self.close()
    
    @property
    def connection(self):
        return self.connection_
    
    @property
    def cursor(self):
        return self.cursor_
    
    def commit(self):
        self.connection.commit()

    def close(self):
        self.commit()
        self.cursor.close()
        self.connection.close()

    def execute(self,sql,params=None):
        self.cursor.execute(sql,params)
    
    def fetchall(self):
        return self.cursor.fetchall()
    
    def fetchone(self):
        return self.cursor.fetchone()
    
    def query(self,sql,params=None):
        self.cursor.execute(sql,params)
        return self.fetchall()