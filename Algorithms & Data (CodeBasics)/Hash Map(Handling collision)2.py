class Hash_Taple:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]  # an array in size 100

    def get_hash(self, key):
        h = 0
        for character in key:
            h += ord(character)

        return h % self.MAX

    def __setitem__(self, key, value):  # allows the syntax : t['']= ...
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break

        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):  # del t['']
        h = self.get_hash(key)
        self.arr[h] = None


t = Hash_Taple()
t['march 6'] = 128
t['march 6'] = 78
t['march 17'] = 459
t['march 8'] = 67
t['march 9'] = 4
print(t['march 6'])
print(t.arr)
