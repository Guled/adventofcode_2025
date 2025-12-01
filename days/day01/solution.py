"""
Advent of Code 2025 - Day 1
"""
from typing import List


def parse_input(input_data: str) -> List[int]:
    """
    Parse the input data.
    
    Args:
        input_data: Raw input string
        
    Returns:
        Parsed data as a list of integers
    """
    lines = input_data.strip().split('\n')
    return [int(line) for line in lines if line]


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
    return sum(data)


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
    return len(data)


if __name__ == "__main__":
    # Read input file
    with open("inputs/day01.txt", "r", encoding="utf-8") as f:
        puzzle_input = f.read()
    
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
