import sys

# print(sys.path)

import re
text = 'Mi numero es 311 123 1212, el codigo del pais es 53, el numero de la suerte es 14'
print(re.findall('[0-9]+', text))

import time
print(time.time())
local_time = time.localtime()
print(time.asctime(local_time))

import collections
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1,4 ,4,6]
counter = collections.Counter(numbers)
print(counter)


