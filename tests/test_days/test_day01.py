"""Tests for Day 1 solutions."""
import pytest
from days.day01.solution import parse_input, part1, part2


class TestDay01:
    """Test cases for Day 1."""
    
    @pytest.fixture
    def sample_input(self):
        """Sample input for testing."""
        return """1
2
3
4
5"""
    
    def test_parse_input(self, sample_input):
        """Test input parsing."""
        result = parse_input(sample_input)
        assert result == [1, 2, 3, 4, 5]
    
    def test_part1(self, sample_input):
        """Test part 1 solution."""
        result = part1(sample_input)
        assert result == 15  # Sum of 1+2+3+4+5
    
    def test_part2(self, sample_input):
        """Test part 2 solution."""
        result = part2(sample_input)
        assert result == 5  # Count of numbers
    
    def test_empty_input(self):
        """Test with empty input."""
        result = parse_input("")
        assert result == []
    
    def test_single_number(self):
        """Test with a single number."""
        result = part1("42")
        assert result == 42
