# Template for New Days

## Solution Template (`days/dayXX/solution.py`)

```python
"""
Advent of Code 2025 - Day XX
"""
from typing import Any


def parse_input(input_data: str) -> Any:
    """
    Parse the input data.
    
    Args:
        input_data: Raw input string
        
    Returns:
        Parsed data in appropriate format
    """
    lines = input_data.strip().split('\n')
    # TODO: Implement input parsing
    return lines


def part1(input_data: str) -> int:
    """
    Solve part 1 of the puzzle.
    
    Args:
        input_data: Raw input string
        
    Returns:
        Solution for part 1
    """
    data = parse_input(input_data)
    # TODO: Implement solution for part 1
    return 0


def part2(input_data: str) -> int:
    """
    Solve part 2 of the puzzle.
    
    Args:
        input_data: Raw input string
        
    Returns:
        Solution for part 2
    """
    data = parse_input(input_data)
    # TODO: Implement solution for part 2
    return 0


if __name__ == "__main__":
    # Read input file
    with open("inputs/dayXX.txt", "r", encoding="utf-8") as f:
        puzzle_input = f.read()
    
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
```

## Test Template (`tests/test_days/test_dayXX.py`)

```python
"""Tests for Day XX solutions."""
import pytest
from days.dayXX.solution import parse_input, part1, part2


class TestDayXX:
    """Test cases for Day XX."""
    
    @pytest.fixture
    def sample_input(self):
        """Sample input from the puzzle description."""
        return """sample input here"""
    
    def test_parse_input(self, sample_input):
        """Test input parsing."""
        result = parse_input(sample_input)
        # TODO: Add assertions
        assert result is not None
    
    def test_part1(self, sample_input):
        """Test part 1 solution."""
        result = part1(sample_input)
        # TODO: Replace with expected value from puzzle
        assert result == 0
    
    def test_part2(self, sample_input):
        """Test part 2 solution."""
        result = part2(sample_input)
        # TODO: Replace with expected value from puzzle
        assert result == 0
```

## Quick Setup Commands

To create a new day (replace XX with day number):

```bash
# Create directories
mkdir -p days/dayXX
mkdir -p tests/test_days

# Create __init__.py
echo '"""Day XX solutions."""' > days/dayXX/__init__.py

# Create empty input file
touch inputs/dayXX.txt

# Copy templates and modify
# Then run: pytest tests/test_days/test_dayXX.py
```
