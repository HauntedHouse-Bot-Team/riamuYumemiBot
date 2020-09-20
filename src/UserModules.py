import os

from src.DbModule import DbModule as db

class UserModules:

    def __init__(self):
        self.db = db()
        self.table = 'ghosts'

    def all_member_register(self, members: list):

        columns = [
            'ghost_id',
            'gold',
        ]

        self.db.multiple_insert(self.table, columns, members)
