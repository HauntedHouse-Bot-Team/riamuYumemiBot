import os

from src.DbModule import DbModule as db

class UserModules:

    def __init__(self):
        self.db = db()
        self.table = 'ghosts'

    def all_member_register(self, members: list):

        columns = [
            'name',
            'ghost_id',
            'gold',
        ]

        self.db.multiple_insert(self.table, columns, members)

    def member_delete(self, member_id: int):
        columns = [
            'del_flg',
        ]
        values = [
            1,
        ]
        narrow_down_column = [
            'ghost_id',
        ]
        narrow_down_values = [
            member_id,
        ]

        self.db.update(self.table, columns, values, narrow_down_column, narrow_down_values)

    def member_undelete(self, member_id: int):
        columns = [
            'del_flg',
        ]
        values = [
            0,
        ]
        narrow_down_column = [
            'ghost_id',
        ]
        narrow_down_values = [
            member_id,
        ]

        self.db.update(self.table, columns, values, narrow_down_column, narrow_down_values)

    def registration_confirm(self, member_id: int):
        sql = 'SELECT * FROM {table} WHERE ghost_id = {ghost_id}'.format(
            table = self.table,
            ghost_id = member_id,
        )

        try:
            response = self.db.select(sql)
        except Exception as e:
            print(e)
            raise

        if not response:
            return False

        return response
