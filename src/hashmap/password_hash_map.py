"""Hashing passwords for authorization"""

import dataclasses

from env.env_constants import USERS_STORAGE
from src.hashmap.hash_map import HashMap
from src.utils.rw import read_from_csv_file, write_data_to_csv_file


@dataclasses.dataclass
class UserPasswordHash:
    """Hashing passwords for authorization"""

    salt: bytes
    hashed_password: bytes


class UserPasswordHashMap(HashMap):
    """Hash map for hide passwords"""

    def store(self, file_path: str = USERS_STORAGE):
        """save hashmap in local storage"""

        password_hash_list = []
        for password in self.buckets:
            if password:
                password_hash_list.append(
                    [
                        password[0][0],
                        password[0][1].salt.hex(),
                        password[0][1].hashed_password.hex(),
                    ]
                )

        write_data_to_csv_file(file_path, password_hash_list)

    def restore_hash_map(self, file_path: str = USERS_STORAGE):
        """Restore hash map from local storage"""

        # read external storage
        data = read_from_csv_file(file_path)

        # revoke buckets
        self.buckets = [[] for _ in range(self.size)]

        for item in data:
            key, salt, hash_password = item
            index = self._hash(key)
            bucket = self.buckets[index]

            # Check if key already exists
            for i, (k, _) in enumerate(bucket):
                if k == key:
                    bucket[i] = (key, UserPasswordHash(salt, hash_password))
                    return

            # Add new key-value pair
            if index <= self.size:
                bucket.append((key, UserPasswordHash(salt, hash_password)))
            else:
                self.size *= 2
                bucket.append((key, UserPasswordHash(salt, hash_password)))
