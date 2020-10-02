from wordcloud import WordCloud
import os
def create_world_cloud(text: list, target = 'all') -> str:
    print(target)
    file_name = f'{target}-fap_material.png'
    file_path = f'./static/WorldCloud/{file_name}'
    wordcloud = WordCloud(background_color="white",
    font_path=os.getenv('FONT_PATH'),
    width=800,height=600).generate(' '.join(text))
    wordcloud.to_file(f'./static/WorldCloud/{file_name}')
    return file_path