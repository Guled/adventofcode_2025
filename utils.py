"""Utility functions for Advent of Code solutions."""
from typing import List


def read_input(filename: str) -> str:
    """Read the entire input file as a string."""
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()


def read_lines(filename: str) -> List[str]:
    """Read input file and return a list of lines (with newlines stripped)."""
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.readlines()]


def read_integers(filename: str) -> List[int]:
    """Read input file and return a list of integers (one per line)."""
    return [int(line) for line in read_lines(filename)]


def read_grid(filename: str) -> List[List[str]]:
    """Read input file as a 2D grid of characters."""
    return [list(line) for line in read_lines(filename)]
