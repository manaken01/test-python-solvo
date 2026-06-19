"""
Tests for the geometric shapes hierarchy.
Do not modify this file.
"""
import pytest
import math
from shapes import Shape, Circle, Rectangle


# ---------------------------------------------------------------------------
# Circle
# ---------------------------------------------------------------------------

def test_circle_area():
    c = Circle(5)
    assert math.isclose(c.area(), math.pi * 25, rel_tol=1e-9)


def test_circle_perimeter():
    c = Circle(5)
    assert math.isclose(c.perimeter(), 2 * math.pi * 5, rel_tol=1e-9)


def test_circle_invalid_radius():
    with pytest.raises(ValueError):
        Circle(0)
    with pytest.raises(ValueError):
        Circle(-3)


def test_circle_repr():
    c = Circle(5)
    assert "Circle" in repr(c)
    assert "5" in repr(c)


# ---------------------------------------------------------------------------
# Rectangle
# ---------------------------------------------------------------------------

def test_rectangle_area():
    r = Rectangle(4, 6)
    assert r.area() == 24


def test_rectangle_perimeter():
    r = Rectangle(4, 6)
    assert r.perimeter() == 20


def test_rectangle_invalid_dimensions():
    with pytest.raises(ValueError):
        Rectangle(0, 5)
    with pytest.raises(ValueError):
        Rectangle(4, -1)


def test_rectangle_repr():
    r = Rectangle(4, 6)
    assert "Rectangle" in repr(r)
    assert "4" in repr(r)
    assert "6" in repr(r)


# ---------------------------------------------------------------------------
# Comparison and sorting
# ---------------------------------------------------------------------------

def test_shapes_sorted_by_area():
    shapes = [Circle(10), Rectangle(2, 3), Circle(1), Rectangle(5, 5)]
    ordered = sorted(shapes)
    areas = [s.area() for s in ordered]
    assert areas == sorted(areas)


def test_shapes_equal_by_area():
    r1 = Rectangle(4, 6)   # area = 24
    r2 = Rectangle(3, 8)   # area = 24
    assert r1 == r2


def test_shapes_not_equal_different_area():
    c = Circle(5)
    r = Rectangle(4, 6)
    assert c != r


def test_shape_lt():
    small = Rectangle(1, 2)   # area = 2
    big = Circle(10)           # area ~ 314
    assert small < big
    assert not big < small


# ---------------------------------------------------------------------------
# Abstraction
# ---------------------------------------------------------------------------

def test_shape_is_abstract():
    """Shape must not be instantiable directly."""
    with pytest.raises(TypeError):
        Shape()
