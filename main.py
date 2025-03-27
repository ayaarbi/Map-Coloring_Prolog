import bridge  # Import bridge module to interface Python with Prolog for graph coloring
import plot  # Import plot module to visualize the colored graph
import matplotlib.pyplot as plt  # Import Matplotlib to display a comparative performance graph


def main():
    """Main function that runs coloring algorithms and compares their performance."""
    input_file = "map.txt"  # Name of the file containing the graph definition (regions and adjacencies)
    output_file = "solution.txt"  # Name of the file where the coloring solution will be saved

    algorithms = ["clp", "clp_mrv"]  # List of coloring algorithms to test
    times = []  # List to store execution times of each algorithm

    # Loop through each algorithm to test its performance
    for algo in algorithms:
        print(f"Testing algorithm: {algo}")  # Display the algorithm being tested
        _, _, elapsed_time = bridge.solve_coloring(input_file, f"solution_{algo}.txt", algorithm=algo)  # Run coloring
        times.append(elapsed_time)  # Store execution time

    # Create a graph to compare algorithm performance
    plt.bar(algorithms, times, color=["blue", "red"])  # Display a bar chart of execution times
    plt.xlabel("Algorithms")  # X-axis label
    plt.ylabel("Execution Time (ms)")  # Y-axis label
    plt.title("Comparison of Coloring Algorithm Performance")  # Graph title
    plt.show()  # Display the graph

    print("Comparison completed!")  # Indicate comparison completion
    print("Reading file and executing Prolog coloring...")  
    result = bridge.solve_coloring(input_file, output_file)  

    if result:
        print("Solution found! Displaying the colored graph...")
        plot.plot_graph(input_file, output_file)  # Display the colored graph
    else:
        print("Error: No solution found.")


if __name__ == "__main__":
    main()  # Call the main function
