import os


def insert(filename, key, value):
    f = open(filename, 'a')
    f.write(key + '\t' + value + '\n')
    f.close()


def select_one(filename, key):
    f = open(filename, 'r')
    for row in f:
        (k, v) = row.split('\t', 1)
        if k == key:
            return v[:-1]
    if v is None:
        return key + " is not in this database"
    f.close()


def delete(filename, key):
    inFile = True
    f = open(filename, 'r')
    result = open('result.txt', 'w')
    for row in f:
        (k, v) = row.split('\t', 1)
        if k != key:
            result.write(row)
        if key not in row:
            inFile = False
        else:
            inFile = True
    if not inFile:
        print(key + " is not in this database")
        return True
    f.close()
    result.close()
    os.replace('result.txt', filename)


def update(filename, key, value=''):
    inFile = True
    f = open(filename, 'r')
    result = open('result.txt', 'w')
    for row in f:
        (k, v) = row.split('\t', 1)
        if k == key:
            result.write(key + '\t' + value + '\n')
        else:
            result.write(row)
        if key not in row:
            inFile = False
        else:
            inFile = True
    if not inFile:
        print(key + " is not in this database")
        return True
    f.close()
    result.close()
    os.replace('result.txt', filename)


os.getcwd()
