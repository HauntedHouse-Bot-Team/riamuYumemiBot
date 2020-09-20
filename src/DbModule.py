import mysql.connector as connector
import configparser
import os

class DbModule:

    def __db_connect(self):
        base = os.path.dirname(os.path.abspath(__file__))
        conf_path = os.path.normpath(os.path.join(base, '../'))
        conf = configparser.ConfigParser()
        conf.read(conf_path+'/config/config.ini', encoding='utf-8')
        try:
            db = connector.connect(
                user = os.getenv('DB_USER'),
                passwd = os.getenv('DB_PASSWORD'),
                host = os.getenv('DB_HOST'),
                db = os.getenv('DB_DATABASE'),
            )
            return db
        except Exception as e:
            print(e)
            raise

    def insert(self, table: str, values: dict):
        cnx = self.__db_connect()
        cur = cnx.cursor()

        columns = list(values.keys())
        parameters = list(values.values())


        sql = "INSERT INTO `{table}` ({columns}) VALUES ({values})".format(
            table = table,
            columns = ', '.join(columns),
            values =  ', '.join(str('\'' + parameter + '\'') for parameter in parameters)
        )

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
            print(e)
            raise

        return response
