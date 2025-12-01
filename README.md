# Advent of Code 2025

Python solutions for [Advent of Code 2025](https://adventofcode.com/2025).

## Setup

### Prerequisites
- Python 3.12 or higher

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Guled/adventofcode_2025.git
cd adventofcode_2025
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

For development (includes linting and formatting tools):
```bash
pip install -r requirements-dev.txt
```

## Project Structure

```
adventofcode_2025/
├── days/               # Solution files organized by day
│   ├── day01/
│   │   └── solution.py
│   └── ...
├── tests/              # Test files
│   ├── test_days/
│   │   └── test_day01.py
│   └── test_utils.py
├── inputs/             # Puzzle input files
│   └── day01.txt
├── utils.py            # Shared utility functions
├── requirements.txt    # Project dependencies
└── pytest.ini          # Pytest configuration
```

## Usage

### Running Solutions

To run a specific day's solution:
```bash
python -m days.day01.solution
```

### Running Tests

Run all tests:
```bash
pytest
```

Run tests for a specific day:
```bash
pytest tests/test_days/test_day01.py
```

Run tests with coverage:
```bash
pytest --cov=days --cov-report=html
```

### Code Quality

Format code with Black:
```bash
black .
```

Lint code with flake8:
```bash
flake8 days/ tests/ utils.py
```

Type check with mypy:
```bash
mypy days/ utils.py
```

## Adding a New Day

1. Create a new directory under `days/` (e.g., `days/day02/`)
2. Add `__init__.py` and `solution.py` files
3. Create your input file in `inputs/` (e.g., `inputs/day02.txt`)
4. Add tests in `tests/test_days/test_day02.py`

You can use `days/day01/` as a template for the structure.

## Utilities

The `utils.py` module provides helper functions for common tasks:
- `read_input(filename)` - Read entire file as string
- `read_lines(filename)` - Read file as list of lines
- `read_integers(filename)` - Read file as list of integers
- `read_grid(filename)` - Read file as 2D grid of characters

## License

This project is for educational purposes.