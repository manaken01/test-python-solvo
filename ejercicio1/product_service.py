from lru_cache import LRUCache

# Global counter of database calls.
# Tests use this to verify the cache prevents redundant queries.
db_call_count = 0


def _fetch_from_db(product_id: int) -> dict | None:
    """
    Simulate an expensive database query.
    Increments db_call_count on every call.
    Do not modify this function.
    """
    global db_call_count
    db_call_count += 1

    catalog = {
        1: {"id": 1, "name": "Laptop",   "price": 999.99},
        2: {"id": 2, "name": "Mouse",    "price": 29.99},
        3: {"id": 3, "name": "Keyboard", "price": 79.99},
        4: {"id": 4, "name": "Monitor",  "price": 399.99},
    }
    return catalog.get(product_id)


class ProductService:
    """
    Product lookup service backed by an LRU cache.

    Avoids repeated database calls by caching the last `cache_capacity`
    products that were queried.
    """

    def __init__(self, cache_capacity: int = 3):
        """
        Args:
            cache_capacity: maximum number of products to keep in the cache.
        """
        self.cache = LRUCache(cache_capacity)

    def get_product(self, product_id: int) -> dict | None:
        """
        Return the data for the given product id.

        Expected algorithm:
        1. Look up product_id in the cache.
        2. Cache hit  -> return the cached value (do NOT call _fetch_from_db).
        3. Cache miss -> call _fetch_from_db, store the result in the cache,
                         then return it.

        Args:
            product_id: product identifier.

        Returns:
            Dict with product data, or None if the product does not exist.
        """
        value = self.cache.get(product_id)
        if value is not None:
            return value
        else:
            _fetch_from_db(product_id)
            self.cache.put(product_id)
            return value
