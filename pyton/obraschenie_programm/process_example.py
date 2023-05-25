import os
import sys

print(sys.argv)
print(os.environ['PATH'])
print("error", file=sys.stderr)