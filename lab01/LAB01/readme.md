**Lab 01: Algorithm Complexity Analysis**

This laboratory explores different algorithm complexities and measures their execution times.

## Contents
- `lab01.py`: Python script implementing algorithms with different time complexities.

## Requirements
- Python 3.x
- Matplotlib library (`pip install matplotlib`)

## Usage
Install the required dependencies:

```bash
pip install matplotlib
```

Run the script and execute the analysis:

```bash
python lab01.py
```

## Implemented Algorithms

### Algorithm 1 - Unknown Complexity
- Iteratively increases `i` and `s` until `s` reaches `n`.
- Tested with `n` values: 1, 10, 100, 1000, 10000.

### Algorithm 2 - Unknown Complexity
- Contains nested loops, including a while loop with logarithmic iteration.
- Tested with `n` values: 1, 10, 100, 1000.

### Algorithm 3 - Unknown Complexity
- Uses conditional branching inside a nested loop structure.
- Tested with `n` values: 1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000.

## Analysis Process
For each algorithm:
- Execution time is measured for different input sizes.
- Results are plotted to visualize how execution time scales with input size.
- Theoretical complexity is inferred from observed performance.

## Student Information
- **Name:** Arnold Alva Torres
- **Course:** Algorithms and Data Structures

## Prompt Engineering (Example for one algorithm)

### Prompt Entered
Implement an algorithm that iteratively increases `i` and `s` until `s` reaches `n`. Measure its execution time with `n` values: 1, 10, 100, 1000, 10000.

### Prompt Analysis
The original prompt was specific about the algorithm's implementation but did not include details about visualization or analysis.

### Improved Prompt
Implement an algorithm that iteratively increases `i` and `s` until `s` reaches `n`. Measure its execution time with `n` values from 1 to 10,000, visualize the results, and analyze how execution time scales in relation to input size.

## Conclusions
-The empirical results confirm the importance of analyzing algorithm performance beyond theoretical complexity.
-Even small variations in an algorithm’s structure can significantly impact execution time.
-Some algorithms perform efficiently for small inputs but become impractical for larger datasets.
-Visualizing execution times helps identify unexpected inefficiencies in an algorithm’s design.
-Algorithm optimization is crucial in real-world applications where computational resources are limited.
