import hashlib

md5 = input('hash: ')
file = open('wordlist.txt', 'r')

for i in file:

    a = i.encode('utf-8')
    b = hashlib.md5(a.strip()).hexdigest()

    if b == md5:
        print('found it', i)
        break
