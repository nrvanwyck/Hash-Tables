# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''

        index = self._hash_mod(key)

        if self.storage[index] is None:
            self.storage[index] = LinkedPair(key, value)

        else:
            old = self.storage[index]
            self.storage[index] = LinkedPair(key, value)
            self.storage[index].next = old

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        index = self._hash_mod(key)

        if self.storage[index] is None:
            return "Key not found"

        else:
            if self.storage[index].key == key:
                self.storage[index].value = None

            else:
                retrieve_loc = self.storage[index].next
                while retrieve_loc is not None:
                    if retrieve_loc.key == key:
                        retrieve_loc.value = None
                    retrieve_loc = retrieve_loc.next

                if retrieve_loc is None:
                    return "Key not found"

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''

        index = self._hash_mod(key)

        if self.storage[index] is None:
            return None

        else:
            if self.storage[index].key == key:
                return self.storage[index].value

            else:
                retrieve_loc = self.storage[index].next
                while retrieve_loc is not None:
                    if retrieve_loc.key == key:
                        return retrieve_loc.value

                    else:
                        retrieve_loc = retrieve_loc.next

                if retrieve_loc is None:
                    return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''

        resized = HashTable(self.capacity * 2)
        for element in self.storage:
            if element is not None:
                to_insert = element
                while to_insert is not None:
                    resized.insert(to_insert.key, to_insert.value)
                    to_insert = to_insert.next

        self.capacity = resized.capacity
        self.storage = resized.storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
