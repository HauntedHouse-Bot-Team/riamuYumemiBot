import mysql.connector as connector
import os

class DbModule:

    def __db_connect(self):
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
    
    def __get_value(self, values: list):
        return '({parameters})'.format(
            parameters = ', '.join(str('\'' + str(parameter) + '\'') for parameter in values)
        )

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

    def multiple_insert(self, table: str, columns: list, values: list):
        cnx = self.__db_connect()
        cur = cnx.cursor()
        parameters = []
        for value in values:
            parameters.append(self.__get_value(value))

        sql = "INSERT INTO `{table}` ({columns}) VALUES {values}".format(
            table = table,
            columns = ', '.join(columns),
            values =  ', '.join(parameters)
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
        except:
            raise
        return response
        
    def update(self, table: str, columns: list, values: list, narrow_down_column: list = None, narrow_down_values: list = None):
        cnx = self.__db_connect()
        cur = cnx.cursor()

        sql = "UPDATE `{table}` SET ".format(
            table = table
        )
        for index in range(len(columns)):
            sql += "{column} = {value}".format(
                column = columns[index],
                value = values[index],
            )
        if narrow_down_column:
            sql += " WHERE "
            narrow_doan = []
            for index in range(len(narrow_down_column)):
                narrow_doan.append("{column} = {value}".format(
                    column = narrow_down_column[index],
                    value = narrow_down_values[index],
                ))
            sql += ', '.join(narrow_doan)
        
        try:
            cur.execute(sql)
            cnx.commit()
            return True
        except:
            cnx.rollback()
            raise
