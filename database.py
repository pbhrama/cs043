import os


class Simpledb:
    def __init__(self, filename):
        self.filename = filename

    def __repr__(self):
        return "<" + self.__class__.__name__ + " file='" + str(self.filename) + "'>"

    def insert(self, key, value):
        f = open(self.filename, 'a')
        f.write(str(key) + '\t' + str(value) + '\n')
        f.close()

    def select_one(self, key):
        f = open(self.filename, 'r')
        inFile = True
        for row in f:
            (k, v) = row.split('\t', 1)
            if k == key:
                return v[:-1]
                inFile = True
            else:
                inFile = False
        if not inFile:
            return key + " is not in this database"
        f.close()

    def delete(self, key):
        inFile = True
        f = open(self.filename, 'r')
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
            return False
        else:
            f.close()
            result.close()
            os.replace('result.txt', self.filename)
            return True

    def update(self, key, value=''):
        inFile = True
        f = open(self.filename, 'r')
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
        os.replace('result.txt', self.filename)

    os.getcwd()




