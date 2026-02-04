"""Hash Map template"""

from typing import Any


class HashMap:
    """Hash Map template"""

    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key: str) -> int:
        """Returns hash from input string"""

        return hash(key) % self.size

    def put(self, key: str, value: Any) -> None:
        """Put pair key/value into hashmap or update existing key"""

        index = self._hash(key)
        bucket = self.buckets[index]

        # Check if key already exists
        for i, k in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # Add new key-value pair
        if index <= self.size:
            bucket.append((key, value))
        else:
            self.size *= 2
            bucket.append((key, value))

    def get(self, key) -> Any:
        """Get item"""

        index = self._hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(f"Key '{key}' not found")

    def remove(self, key):
        """remove pair key/value from hash map for logout function"""

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

    def print(self):
        """Print hash map"""
        print(self.buckets)
