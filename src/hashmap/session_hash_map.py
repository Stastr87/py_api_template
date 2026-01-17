"""Store user's session hash map"""

from dataclasses import dataclass

from env.env_constants import SESSIONS_STORAGE
from src.hashmap.hash_map import HashMap
from src.utils.rw import read_from_csv_file, write_data_to_csv_file


@dataclass
class SessionInfo:
    """Session info"""

    login: str
    token: str
    expires_in: str


class SessionInfoHashMap(HashMap):
    """Hash map for store user's session info"""

    def store(self, file_path: str = SESSIONS_STORAGE):
        """save hashmap in local storage"""

        for user in self.buckets:
            if user:
                write_data_to_csv_file(
                    file_path,
                    [
                        [
                            user[0][0],
                            user[0][1].login,
                            user[0][1].token,
                            user[0][1].expires_in,
                        ]
                    ],
                )

    def restore_hash_map(self, file_path: str = SESSIONS_STORAGE):
        """Restore hash map from local storage"""

        # read external storage
        data = read_from_csv_file(file_path)

        # revoke buckets
        self.buckets = [[] for _ in range(self.size)]

        for item in data:
            user, login, token, expire_in = item
            index = self._hash(user)
            bucket = self.buckets[index]

            # Check if key already exists
            for i, (k, _) in enumerate(bucket):
                if k == user:
                    bucket[i] = (user, SessionInfo(login, token, expire_in))
                    return

            # Add new key-value pair
            if index <= self.size:
                bucket.append((user, SessionInfo(login, token, expire_in)))
            else:
                self.size *= 2
                bucket.append((user, SessionInfo(login, token, expire_in)))
