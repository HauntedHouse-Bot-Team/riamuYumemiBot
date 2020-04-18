import mysql.connector as connector
import configparser
import os

class MyModules:

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

    def seve_masturbation_log(self, user: str, fap_material: str, guild: str):

        sql = "INSERT INTO `{table}` (user, fap_material, guild) VALUES ('{user}', '{fap_material}', '{guild}')".format(
            table = 'masturbation_log',
            user = user,
            fap_material = fap_material,
            guild = guild
        )

        cnx = self.__db_connect()
        cur = cnx.cursor()
        try:
            cur.execute(sql)
            cnx.commit()
        except:
            cnx.rollback()
            raise
