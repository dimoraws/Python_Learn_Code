# python3 arguments.py --temperature=20 --pressure=170 --today=25.05.2023

import sys

print(sys.argv)
for arg in sys.argv:
    print(arg)