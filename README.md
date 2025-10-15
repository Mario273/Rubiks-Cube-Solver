# Rubik's Cube Solver

A Python program that models and solves a Rubik’s Cube.  

## Project Status

This project is in development.  
Currently, the cube can:
- Perform all basic turns (`R`, `L`, `U`, `D`, `F`, `B` and their inverses)
- Scramble itself randomly
- Display an ASCII representation of its current state
- Perform helper operations (e.g., get position of piece, convert user input to list of moves)

The next step is to finish the solver function, which will use the standard beginner’s method to find a solution.  
After that, I plan to build an interface to use all cube features more easily.

## Implementation Details

- The cube’s internal state is stored in two arrays; one for edge pieces, and 1 for corner pieces
- each piece has a position and orientation
- Written entirely in Python (no external dependencies)
- Currently contained in a single file: `main.py`

## Usage

Run the program directly:

```bash
python main.py
