"""Hashing passwords for authorization"""

from src.hashmap.encryption import encryption_srt
from src.utils.rw import read_from_csv_file, write_data_to_csv_file


class HashMap:
    """Hash map for hide passwords"""

    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key: str) -> int:
        """Returns hash from input string"""
        return hash(key) % self.size

    def put(self, key: str, value: str):
        """Put pair key/value into hashmap or update existing key"""
        index = self._hash(key)
        bucket = self.buckets[index]

        # Check if key already exists
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, encryption_srt(value).hex())
                return

        # Add new key-value pair
        if index <= self.size:
            bucket.append((key, encryption_srt(value).hex()))
        else:
            self.size *= 2
            bucket.append((key, encryption_srt(value).hex()))

    def get(self, key):
        """Get value from hashmap"""
        index = self._hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(f"Key '{key}' not found")

    def remove(self, key):
        """remove pair key/value from hash map"""
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        raise KeyError(f"Key '{key}' not found")

    def __contains__(self, key):
        """Check existing key in hashmap object"""
        index = self._hash(key)
        bucket = self.buckets[index]

        for k, _ in bucket:
            if k == key:
                return True
        return False

    def store(self):
        """save hashmap in local storage"""

        for item in self.buckets:
            if item:

                write_data_to_csv_file("tmp/hs.csv", item)

    def restore_hash_map(self):
        """Read hash map from local storage"""

        # read external storage
        data = read_from_csv_file("tmp/hs.csv")

        # revoke buckets
        self.buckets = [[] for _ in range(self.size)]

        for item in data:
            key, value = item
            index = self._hash(key)
            bucket = self.buckets[index]

            # Check if key already exists
            for i, (k, _) in enumerate(bucket):
                if k == key:
                    bucket[i] = (key, value)
                    return

            # Add new key-value pair
            if index <= self.size:
                bucket.append((key, value))
            else:
                self.size *= 2
                bucket.append((key, value))


# Usage
my_map = HashMap()
# my_map.put("apple", "aa")
# my_map.put("admin", "admin")
# my_map.put("odmin1", "odmin")
# my_map.put("odmin2", "odmin")
# my_map.put("odmin3", "odmin")
# my_map.put("odmin4", "odmin")
# my_map.put("odmin5", "odmin")
# my_map.put("odmin6", "odmin")
# my_map.put("odmin7", "odmin")
# my_map.put("odmin8", "odmin")
# my_map.put("odmin9", "odmin")
# my_map.put("odmin10", "odmin")
# my_map.put("odmin11", "odmin")
# print(my_map.get("apple"))  # 5
# print("apple" in my_map)  # True
# my_map.store()

my_map.restore_hash_map()
print(my_map.get("admin"))
print(my_map.get("odmin1"))
print(my_map.get("odmin11"))
print(my_map.get("apple"))
print(my_map.get("apple1"))
print(my_map.get("apple1"))
