# пример ловли исключения при делении на 0
def division():
    try:
        a = 3/0
        print(a)
    except:
        print('na 0 delit nelza')

# пример чтения из файла, и если такого файла нет - то создание его
def read_or_create1():
    filename = 'this_file_not_exist.txt'
    try:
        with open(filename) as f:
            return f.read()
    except FileNotFoundError:
        with open(filename, 'w') as f:
            pass

# пример чтения 
import os.path
def read_or_create2():
    filename = 'this_file_not_exist.txt'
    if os.path.isfile(filename):
        with open(filename) as f:
            return f.read()
    else:
        with open(filename, 'w') as f:
            pass
read_or_create2()