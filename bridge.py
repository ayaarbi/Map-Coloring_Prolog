from pyswip import Prolog  # Import PySwip to interface Python with SWI-Prolog
import time  # Import time library to measure execution time


def read_graph(file_path):
    """Reads a map and returns the regions and adjacencies.
       Takes a file as input and returns the regions and adjacencies as lists."""
    regions = set()  # Use a set to store regions to avoid duplicates
    adjacencies = []  # List of adjacency relations between regions

    with open(file_path, "r") as file:  # Open the file in read mode
        for line in file:  # Iterate through each line in the file
            parts = line.strip().split("(")  # Split the line at the first parenthesis
            if len(parts) > 1:
                args = parts[1].replace(").", "").split(",")  # Clean the line and extract arguments
                args = [arg.strip() for arg in args]  # Remove unnecessary spaces

                if "region" in parts[0]:  # Check if the line defines a region
                    regions.add(args[0])  # Add the region to the set of regions
                elif "adjacent" in parts[0]:  # Check if the line defines an adjacency relation
                    adjacencies.append((args[0], args[1]))  # Add adjacency to the list

    return list(regions), adjacencies  # Convert the set to a list and return regions and adjacencies


def solve_coloring(input_file, output_file, algorithm="clp"):
    """Runs the chosen coloring algorithm and saves the result."""
    regions, adjacencies = read_graph(input_file)  # Read the graph from the file

    prolog = Prolog()  # Initialize an instance of SWI-Prolog
    prolog.consult("graph_coloring.pl")  # Load the Prolog file containing coloring algorithms

    algorithms = {  # Associate each algorithm with its corresponding Prolog predicate
        "clp": "color_graph_clp",  # Basic CLP(FD) coloring algorithm
        "clp_mrv": "color_graph_clp_mrv"  # CLP(FD) with Minimum Remaining Values (MRV)
    }

    if algorithm not in algorithms:
        print("Error: Unknown algorithm. Choose from:", list(algorithms.keys()))
        return None  # Return None if the specified algorithm does not exist

    algo_predicate = algorithms[algorithm]  # Retrieve the corresponding Prolog predicate
    query = f"{algo_predicate}({regions}, {adjacencies}, Coloring)."  # Form the Prolog query

    start_time = time.time()  # Record the start time
    result = list(prolog.query(query))  # Execute the Prolog query and retrieve results
    elapsed_time = (time.time() - start_time) * 1000  # Calculate elapsed time in milliseconds

    if result:  # Check if a solution was found
        coloring = result[0]["Coloring"]  # Retrieve the list of assigned colors
        with open(output_file, "w") as file:  # Open the output file in write mode
            for region, color in zip(regions, coloring):  # Associate each region with its color
                file.write(f"{region} -> Color {color}\n")  # Save the solution in the file
        print(f"Solution saved in {output_file} ({algorithm.upper()}) in {elapsed_time:.2f} ms")
        return regions, coloring, elapsed_time  # Return regions, coloring, and execution time
    else:
        print("Error: No solution found.")
        return None  # Return None if no solution was found
