from abc import ABC, abstractclassmethod

import hashlib
import random
import string


class BaseShort(ABC):
    @abstractclassmethod
    def __init__(self):
        pass
    @abstractclassmethod
    def check_short(self, long_url):
        pass
    @abstractclassmethod
    def short(self, long_url):
        pass
    @abstractclassmethod
    def store_data(self, long_url):
        pass
    @abstractclassmethod
    def get(self, short_url):
        pass
    
class BaseURLShort(BaseShort):
    
    def __init__(self, limit):
        self.limit = limit
        self.data_store = {}
        self.data_search = {}
        
    def get(self, short_url):
        
        if short_url not in self.data_search:
            raise Exception("Not found!")
        
        return self.data_search[short_url]
    
    def check_short(self, long_url):
        
        if long_url in self.data_store:
            return self.data_store[long_url]
        
        if len(self.data_store.keys()) == self.limit:
            raise Exception("Limit reached")
        
        return None
    

    def create_url(self, long_url):
        
        hash_object = hashlib.md5(long_url.encode("utf-8"))
        hash_value = hash_object.hexdigest()[:10]
        return hash_value
        
        
    def short(self, long_url):
        result = self.check_short(long_url)
        
        if result:
            return result
        
        short_url = self.create_url(long_url)
        self.store_data(long_url, short_url)
        return short_url
    
    def store_data(self, long_url, short_url):
        self.data_search[short_url] = long_url
        self.data_store[long_url] = short_url
        
        
class RandomListURLShort(BaseURLShort):
    
    def __init__(self, **kwargs):
        super().__init__(kwargs)
        limit = kwargs[limit]
        self.hash_list = [''.join(random.choice(string.ascii_uppercase + string.digits)) for _ in range(limit) for _ in range(limit)]
    

    def create_url(self, long_url):
        
        if not self.hash_list:
            raise Exception("Hash List is empty!")
        hash_string = self.hash_list.pop()
        
        return hash_string
        
            

