import os

for i in os.environ:
    print(i, os.environ.get(i))
# print(os.environ.get('TEMP'))
