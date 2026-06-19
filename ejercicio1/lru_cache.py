class LRUCache:
    """
    Cache with a Least Recently Used (LRU) eviction policy.

    When capacity is exceeded, the least recently used entry is removed.

    Mandatory constraints:
    - Do NOT use collections.OrderedDict
    - Do NOT use functools.lru_cache or @cache
    - get() and put() must run in O(1) average time

    Usage example:
        cache = LRUCache(capacity=2)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.get("a")    # -> 1  ("a" is now the most recently used)
        cache.put("c", 3) # capacity exceeded -> evicts "b" (least recently used)
        cache.get("b")    # -> None (evicted)
        cache.get("a")    # -> 1
        cache.get("c")    # -> 3
    """

    def __init__(self, capacity: int):
        """
        Args:
            capacity: maximum number of entries the cache can hold. Guaranteed >= 1.
        """
        # TODO: implement
        self.capacity = capacity
        self.cache = {}
        self.recent = ""


    def get(self, key):
        """
        Return the value associated with key.

        If key exists, mark it as recently used and return its value.
        If key does not exist, return None.

        Args:
            key: hashable key to look up.

        Returns:
            The stored value, or None if not found.
        """
        # TODO: implement
        if (key in self.cache[key]):
            self.recent = key
            return self.cache[key].value
        else:
            return None


    def put(self, key, value) -> None:
        """
        Insert or update key with value.

        If key already exists, update its value and mark it as recently used.
        If key is new and the cache is at capacity, evict the least recently
        used entry before inserting the new one.

        Args:
            key: hashable key.
            value: value to store.
        """
        # TODO: implement

        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.pop(next(iter(self.cache)))