import re
from typing import Collection

reg = re.compile('^(c|C)[0-9]+$')
column = input()
if reg.match(column):
    print(column)
else:
    print('형식 에러')
