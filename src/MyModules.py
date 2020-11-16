import mysql.connector as connector
import os

from google.cloud import vision

from src.DbModule import DbModule as db
from src.PictureDownload import picture_download

class MyModules:

    def __init__(self):
        self.db = db()
        self.table  = 'masturbation_log'

    def text_detection(self, url: str):

        file_path = picture_download(url)
        client = vision.ImageAnnotatorClient()

        with open(file_path, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)
        response = client.text_detection(image=image)
        texts = response.text_annotations

        return texts[0].description

    def seve_masturbation_log(self, user: str, fap_material: str, guild: str):

        try:
            self.db.insert(self.table, {
                'user': user,
                'fap_material': fap_material,
                'guild': guild
            })
            return True
        except:
            raise

    def get_count_list_by_guild(self):

        sql = 'SELECT guild, COUNT(guild) as count FROM {table} GROUP BY guild  ORDER BY count DESC'.format(
            table = self.table
        )

        try:
            response = self.db.select(sql)
        except Exception as e:
            print(e)
            raise

        return response

    def get_count_list_by_user(self):

        sql = 'SELECT user, COUNT(guild) as count FROM {table} GROUP BY user ORDER BY count DESC'.format(
            table = self.table
        )

        try:
            response = self.db.select(sql)
        except Exception as e:
            print(e)
            raise

        return response

    def get_count_list_by_fap_material(self):

        sql = 'SELECT fap_material ,COUNT(fap_material) as count FROM {table} GROUP BY fap_material ORDER BY count DESC'.format(
            table = self.table
        )

        try:
            response = self.db.select(sql)
        except Exception as e:
            print(e)
            raise

        return response

    def get_list_by_otaku_fap_material(self, user):

        sql = "SELECT user, fap_material, COUNT(fap_material) as count from {table} WHERE user = '{user}' GROUP BY fap_material ORDER BY count DESC".format(
            table = self.table,
            user = user,
        )

        try:
            response = self.db.select(sql)
        except Exception as e:
            print(e)
            raise

        return response

    async def create_channel(self, ctx, duplication_source_channel, channel_name):
        #category_id = ctx.channel.category_id
        #category = ctx.guild.get_channel(category_id)
        try:
            new_channel = await duplication_source_channel.clone(name=channel_name)
            return new_channel
        except Exception as e:
            print(e)
            return False

    async def delete_channel(self, ctx, reason):
        try:
            await ctx.channel.delete(reason=reason)
            return True
        except Exception as e:
            print(e)
            return False

    async def load_fap_material(self) -> list:
        sql = f'SELECT fap_material FROM {self.table}'

        try:
            response = self.db.select(sql)
        except Exception as e:
            print(e)
            raise

        return response

    async def get_fap_material_of_nard(self, target: str) -> list:
        sql = f"SELECT fap_material FROM {self.table} WHERE user = '{target}'"

        try:
            response = self.db.select(sql)
        except Exception as e:
            print(e)
            raise

        return response
