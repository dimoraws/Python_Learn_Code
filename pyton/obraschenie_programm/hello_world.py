# Обращение к внешнеей переменной окружения
# Linux\Mac: export USER_NAME=DIMA
# Windows: set USER_NAME=DIMA

import os
username = os.environ['USER_NAME']
print('Привет:', username)