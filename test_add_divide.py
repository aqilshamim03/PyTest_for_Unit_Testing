from add_divide import add, divide
import pytest

def test_add():
    assert add(2, 3) == 5, "Expected 2 + 3 to equal 5"
    assert add(-1, 1) == 0, "Expected -1 + 1 to equal 0"
    assert add(0, 0) == 0, "Expected 0 + 0 to equal 0"

def test_divide():
    with pytest.raises (ValueError, match="Cannot divide by zero"):
        divide(10, 0)