"""
Tests for ProductService and LRUCache.
Do not modify this file.
"""
import pytest
import product_service as ps
from product_service import ProductService


@pytest.fixture(autouse=True)
def reset_db_counter():
    """Reset the DB call counter before each test."""
    ps.db_call_count = 0
    yield


def test_cache_miss_calls_db():
    """First lookup must hit the database."""
    service = ProductService(cache_capacity=3)
    product = service.get_product(1)
    assert product["name"] == "Laptop"
    assert ps.db_call_count == 1


def test_cache_hit_does_not_call_db():
    """A second lookup for the same product must not call the database."""
    service = ProductService(cache_capacity=3)
    service.get_product(1)
    service.get_product(1)
    assert ps.db_call_count == 1


def test_different_products_each_call_db():
    """Each distinct uncached product must trigger one DB call."""
    service = ProductService(cache_capacity=3)
    service.get_product(1)
    service.get_product(2)
    service.get_product(3)
    assert ps.db_call_count == 3


def test_lru_eviction():
    """
    With capacity 2, the least recently used entry is evicted
    when a third product is requested.
    """
    service = ProductService(cache_capacity=2)
    service.get_product(1)  # cache: [1]
    service.get_product(2)  # cache: [1, 2]
    service.get_product(3)  # full -> evicts 1 -> cache: [2, 3]
    assert ps.db_call_count == 3

    # Product 1 was evicted, must go to DB again
    service.get_product(1)
    assert ps.db_call_count == 4


def test_recently_accessed_survives_eviction():
    """
    Accessing an entry promotes it to most-recently-used;
    it must not be evicted on the next insertion.
    """
    service = ProductService(cache_capacity=2)
    service.get_product(1)  # cache: [1]
    service.get_product(2)  # cache: [1, 2]
    service.get_product(1)  # promotes 1 -> cache: [2, 1]  (2 is now LRU)
    service.get_product(3)  # evicts 2 -> cache: [1, 3]
    assert ps.db_call_count == 3  # products 1, 2, 3 — second get(1) was a hit

    # Product 1 is still cached
    service.get_product(1)
    assert ps.db_call_count == 3  # no new DB call


def test_nonexistent_product_returns_none():
    """A product_id not in the catalog must return None."""
    service = ProductService(cache_capacity=3)
    result = service.get_product(999)
    assert result is None
