from abc import ABC, abstractclassmethod

import hashlib
import random
import string


class BaseShort(ABC):
    @abstractclassmethod
    def __init__(self):
        pass

    @abstractclassmethod
    def _check_short(self, long_url):
        pass

    @abstractclassmethod
    def short(self, long_url):
        pass

    @abstractclassmethod
    def _store_data(self, long_url):
        pass

    @abstractclassmethod
    def _create_url(self, long_url):
        """The only method that should be overwritten in derived class"""
        pass

    @abstractclassmethod
    def get(self, short_url):
        pass


class BaseURLShort(BaseShort):
    def __init__(self, limit):
        self._limit = limit
        self._data_store = {}
        self._data_search = {}

    def get(self, short_url):
        if short_url not in self._data_search:
            raise Exception("Not found!")

        return self._data_search[short_url]

    def _check_short(self, long_url):
        if long_url in self._data_store:
            return self._data_store[long_url]

        if len(self._data_store.keys()) == self._limit:
            raise Exception("Limit reached")

        return None

    def _create_url(self, long_url=None):
        hash_object = hashlib.md5(long_url.encode("utf-8"))
        hash_value = hash_object.hexdigest()[:10]
        return hash_value

    def short(self, long_url):
        result = self._check_short(long_url)

        if result:
            return result

        short_url = self._create_url(long_url)
        self._store_data(long_url, short_url)
        return short_url

    def _store_data(self, long_url, short_url):
        self._data_search[short_url] = long_url
        self._data_store[long_url] = short_url


class RandomListURLShort(BaseURLShort):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._hash_list = [
            "".join(
                [
                    random.choice(string.ascii_uppercase + string.digits)
                    for _ in range(10)
                ]
            )
            for _ in range(self._limit)
        ]

    def _create_url(self, long_url):
        if not self._hash_list:
            raise Exception("Hash List is empty!")
        hash_string = self._hash_list.pop()

        return hash_string
