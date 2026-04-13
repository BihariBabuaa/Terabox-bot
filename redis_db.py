import logging

log = logging.getLogger("telethon")

class Redis:
    def __init__(self, *args, **kwargs):
        self._cache = {}
        self.logger = log

    def get_key(self, key):
        return self._cache.get(key)

    def set_key(self, key, value=None):
        self._cache[key] = value
        return value

    def del_key(self, key):
        if key in self._cache:
            del self._cache[key]
        return True

db = Redis()
