import requests
import os
from datetime import datetime

def picture_download(url: str):    
    r = requests.get(url, stream=True)
    file_name = '/{time}.jpg'.format(
        time = datetime.now().strftime('%Y%m%d%H%M%S')
    )
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.normpath(os.path.join(base_path, '../static/UploadImages')) + file_name
    if r.status_code == 200:
        try:
            with open(file_path, 'wb') as f:
                f.write(r.content)
            return file_path
        except Exception as e:
            print(e)
            raise
