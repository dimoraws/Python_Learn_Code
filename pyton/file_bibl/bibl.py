import json
from pprint import pprint

def movie():
    with open('GodFather.json') as godfather_file:
        movie = json.load(godfather_file)
        pprint(movie)

coutries = [
    {"name": "Russia"},
    {"name": "USA"}
]

# Создание файла на JSON
def country():
    with open('example_save.json', 'w') as example_file:
        json.dump(coutries, example_file)