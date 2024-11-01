#!/usr/bin/env python3

"""Task: FIFO caching
"""


from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A class 'FIFOCAche' that inherits from
    'BaseCaching' and its a caching system.
    """

    def __init__(self):
        """initialize the FIFO cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache using vivo"""
        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"Discard: {first_key}")

        self.cache_data[key] = item

    def get(self, key):
        """return the value in 'self.cache_data' linked to 'key'
        """
        return self.cache_data.get(key, None)
