class HashTable:
    def __init__(self, size=7) -> None:
        self.data_map = [None] * size

    def __hash(self, key):
        """Hashing function"""
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        lst = self.data_map[index]
        if lst:
            for i in lst:
                if i[0] == key:
                    return i[1]
        return None

    def keys(self):
        keys = []
        for items in self.data_map:
            if items:
                for k in items:
                    keys.append(k[0])
        return keys


my_hash_table = HashTable()

my_hash_table.set_item("bolts", 1400)
my_hash_table.set_item("washers", 50)

print("Bolts:", my_hash_table.get_item("bolts"))
print("Washers:", my_hash_table.get_item("washers"))
print("Lumber:", my_hash_table.get_item("lumber"))

print(my_hash_table.keys())
"""
    EXPECTED OUTPUT:
    ----------------
    Bolts: 1400
    Washers: 50
    Lumber: None

"""
