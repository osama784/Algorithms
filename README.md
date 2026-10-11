# Algorithms

Personal practice collection of algorithms and problem-solving exercises in Python, written while working through courses, tutorials, and practice problem sets.

## What it is

A folder dump of exercise scripts — not a library or package. Each top-level folder groups scripts by the course or topic they came from, and each file is a standalone script (many end with a small demo/`print` call). Some folders have an `exercises/` subfolder with additional tasks and sample data.

Topics covered:

- **Data structures:** arrays, linked lists, stacks, queues, hash maps, trees, binary search trees, graphs
- **Sorting:** bubble, selection, insertion, merge, quick
- **Searching:** linear, binary, recursive binary
- **Recursion:** factorial, Fibonacci
- **Dynamic programming:** memoization and tabulation variants (can-sum, best-sum, grid-traveller style problems)
- **Greedy algorithms:** activity selection, gas station, meeting rooms, and more
- **Pattern searching**

There is also a `concepts/` folder with reference diagrams (PNG); IDE project files (`.idea/`) live at the repo root, and a few sample data files (`nyc_weather.csv`, `poem.txt`) are inside the `Algorithms & Data (CodeBasics)` folder.

## Running a script

No packaging (`requirements.txt`, `pyproject.toml`, etc.) and no test suite — run any script directly with Python 3:

```bash
python "path/to/script.py"
```

Most scripts use only the standard library; one exercise imports `pandas`.

## Context

This is learning/practice code kept as-is for reference. It is not maintained as a reusable library, and code quality varies by exercise.
