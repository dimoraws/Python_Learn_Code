import subprocess

print('--------------')
e = subprocess.run(['python3', 'obraschenie_programm/process_example.py'])
e.check_returncode()
print('##################')
print('Код возврата:', e.returncode)
print(type(e))
# print(dir(e))
print(e)
print('Программа напечатала:')
print(e.stdout)