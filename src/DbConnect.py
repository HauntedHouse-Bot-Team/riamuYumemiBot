import mysql.connector as connector
import configparser
import os

class DbConnect:

    def __db_connect(self):
        base = os.path.dirname(os.path.abspath(__file__))
        conf_path = os.path.normpath(os.path.join(base, '../'))
        conf = configparser.ConfigParser()
        conf.read(conf_path+'/config/config.ini', encoding='utf-8')
        try:
            db = connector.connect(
                user = conf['DATABASE']['USER'],
                passwd = conf['DATABASE']['PASSWD'],
                host = conf['DATABASE']['HOST'],
                db = conf['DATABASE']['DB_NAME'],
            )
            return db
        except Exception as e:
            print(e)
            raise

    def insert(self, sql: str):
        cnx = self.__db_connect()
        cur = cnx.cursor()
        try:
            cur.execute(sql)
            cnx.commit()
            return True
        except:
            cnx.rollback()
            raise

    def select(self, sql: str):
        cnx = self.__db_connect()
        cur = cnx.cursor(dictionary=True)
        try:
            cur.execute(sql)
            response = cur.fetchall()
            cur.close()
        except Exception as e:
            raise

        return response
