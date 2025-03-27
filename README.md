# Graph Coloring Using Prolog, CLP(FD), and PySwip

## Overview
This project focuses on solving the **graph coloring problem** using **Prolog** and **Constraint Logic Programming over Finite Domains (CLP(FD))**. It integrates with **Python** using **PySwip**, enabling interaction between Prolog and Python for processing graph data and visualization. The goal is to apply different graph coloring algorithms and compare their efficiency.

## Technologies Used
- **Prolog**: Logic programming language used to define constraints and solve the graph coloring problem.
- **CLP(FD)**: A constraint solver for finite domain problems in Prolog.
- **PySwip**: A Python library that enables interaction with Prolog using SWI-Prolog.
- **NetworkX**: Used in Python to represent and visualize graphs.
- **Matplotlib**: For visualizing the colored graph.

## How It Works
1. **Defining the Graph in Prolog**:
   - The graph is represented using `region/1` and `adjacent/2` predicates.
   - Example:
     ```prolog
     region(a).
     region(b).
     adjacent(a, b).
     ```
2. **Solving the Graph Coloring Problem**:
   - The `color_graph/1` predicate assigns colors to each region while ensuring no two adjacent regions have the same color.
   - The implementation uses `CLP(FD)` for constraint satisfaction.
3. **Interacting with Python**:
   - Python (via PySwip) reads the graph definition from a file.
   - It invokes Prolog to find a valid coloring solution.
   - The solution is read and visualized using NetworkX and Matplotlib.



## Installation & Setup
### Prerequisites
- Install **SWI-Prolog**: [Download](https://www.swi-prolog.org/Download.html)
- Install Python and required libraries:
  ```sh
  pip install pyswip networkx matplotlib
  ```

### Running the Project

   **you just need to access the project directory and type**:
   ```sh
   python main.py
   ```

## Features
- Two graph coloring heuristics.
- Constraint-based solving with **CLP(FD)**.
- Python integration for **visualization and analysis**.
- Easily customizable for different graph structures.

## Future Enhancements
- Implement additional heuristics for improved performance.
- Extend support for dynamic graph input formats.
- Compare execution times of different algorithms.

## License
This project is open-source under the MIT License.

