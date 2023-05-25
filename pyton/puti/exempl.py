# with open('myfile.txt') as f:
#     print(f.read())

import os.path

dir_path = os.path.dirname(os.path.relpath(__file__))
coutries_path = os.path.join(dir_path, 'countries.txt')

print(coutries_path)
with open(coutries_path) as countries:
    for country in countries:
        print(country)