__author__ = """730761985"""
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from exercises.ex03.dictionary import invert, count, favorite_color, bin_len
import pytest

# Invert tests


# Use Case 1: swaps keys and values
def test_invert_use_case_1():
    """Invert swaps keys and values in a normal use case."""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


# Use Case 2: handles single value
def test_invert_use_case_2():
    """Invert handles a single key value pair."""
    assert invert({"one": "first"}) == {"first": "one"}


# Edge Case: raises key error due to duplicates
def test_invert_edge_case():
    """Invert raises a KeyError with duplicate values encountered."""
    with pytest.raises(KeyError):
        invert({"kris": "jordan", "michael": "jordan"})


# count tests


# Use Case 1: properly counts
def test_count_use_case_1():
    """Count properly counts occurrences in a list."""
    assert count(["apple", "banana", "apple", "orange", "banana", "banana"]) == {
        "apple": 2,
        "banana": 3,
        "orange": 1,
    }


# Use Case 2: all unique elements
def test_count_use_case_2():
    """Count handles a list with all unique elements."""
    assert count(["red", "blue", "green"]) == {"red": 1, "blue": 1, "green": 1}


# Edge Case: empty list
def test_count_edge_case():
    """Count returns an empty dictionary when given an empty list."""
    assert count([]) == {}


# -favorite_color tests


# Use Case 1: returns most common color
def test_favorite_color_use_case_1():
    """Favorite color returns the most common color in a normal case."""
    assert (
        favorite_color({"Alice": "blue", "Bob": "green", "Charlie": "blue"}) == "blue"
    )


# Use Case 2: returns first color in a tie
def test_favorite_color_use_case_2():
    """Favorite color returns the first color in a tie."""
    assert (
        favorite_color({"Alice": "blue", "Bob": "green", "Charlie": "green"}) == "green"
    )


# Edge Case: empty dictionary
def test_favorite_color_edge_case():
    """Favorite color returns an empty string when given an empty dictionary."""
    assert favorite_color({}) == ""


# bin_len tests


# Use Case 1: groups words by length
def test_bin_len_use_case_1():
    """Bin length groups words by their length."""
    assert bin_len(["apple", "banana", "cat", "dog"]) == {
        5: {"apple"},
        6: {"banana"},
        3: {"cat", "dog"},
    }


# Use Case 2: words of same length
def test_bin_len_use_case_2():
    """Bin length handles words of the same length."""
    assert bin_len(["hi", "to", "up"]) == {2: {"hi", "to", "up"}}


# Edge Case: empty list
def test_bin_len_edge_case():
    """Bin length returns an empty dictionary when given an empty list."""
    assert bin_len([]) == {}
