"""Tests for utility functions."""
import pytest
import tempfile
import os
from utils import read_input, read_lines, read_integers, read_grid


class TestUtils:
    """Test cases for utility functions."""
    
    @pytest.fixture
    def temp_file(self):
        """Create a temporary file for testing."""
        fd, path = tempfile.mkstemp(text=True)
        yield path
        os.close(fd)
        os.unlink(path)
    
    def test_read_input(self, temp_file):
        """Test read_input function."""
        content = "line1\nline2\nline3"
        with open(temp_file, 'w') as f:
            f.write(content)
        
        result = read_input(temp_file)
        assert result == content
    
    def test_read_lines(self, temp_file):
        """Test read_lines function."""
        with open(temp_file, 'w') as f:
            f.write("line1\nline2\nline3\n")
        
        result = read_lines(temp_file)
        assert result == ["line1", "line2", "line3"]
    
    def test_read_integers(self, temp_file):
        """Test read_integers function."""
        with open(temp_file, 'w') as f:
            f.write("1\n2\n3\n42\n")
        
        result = read_integers(temp_file)
        assert result == [1, 2, 3, 42]
    
    def test_read_grid(self, temp_file):
        """Test read_grid function."""
        with open(temp_file, 'w') as f:
            f.write("abc\ndef\nghi\n")
        
        result = read_grid(temp_file)
        assert result == [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i']
        ]
