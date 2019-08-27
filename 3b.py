import string 
from random import randint
str = string.printable

for i in range(6):
    print(str[randint(0,100)],end="")


