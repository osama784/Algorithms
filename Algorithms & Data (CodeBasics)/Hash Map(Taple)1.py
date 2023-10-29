# i understood it, just see the vireo again

class Hash_Taple:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]  # an array in size 100

    def get_hash(self, key):
        h = 0
        for character in key:
            h += ord(character)

        return h % self.MAX

    def __setitem__(self, key, value):  # allows the syntax : t['']= ...
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):  # del t['']
        h = self.get_hash(key)
        self.arr[h] = None


t = Hash_Taple()
print(t.get_hash('march 6'))

t['march 7'] = 130
t['march 1'] = 20
t['december 17'] = 27

print(t['march 6'])
print(t['december 17'])

# print(t.arr)

t['march 8'] = 56
del t['march 8']
print(t['march 8'])