# Write your test here
from challenge03 import conver_to_BTS,print_BTS
import pytest

def test_conver_to_BTS_empty():
    nums = []
    root = conver_to_BTS(nums)
    assert root is None

def test_conver_to_BTS_non_empty():
    nums = [1, 2, 3, 4, 5, 6, 7]
    root = conver_to_BTS(nums)
    expected_output = [4, 2, 6, 1, 3, 5, 7]
    assert print_BTS(root) == expected_output

if __name__ == "__main__":
    main()

