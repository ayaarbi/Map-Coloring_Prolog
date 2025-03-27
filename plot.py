import networkx as nx  # Imports the NetworkX library for managing and visualizing graphs
import matplotlib.pyplot as plt  # Imports Matplotlib to display the colored graph


def read_solution(file_path):
    """Reads the coloring solution from a file and returns a dictionary mapping each region to a color."""
    colors = {}  # Dictionary to store the association between regions and their colors
    with open(file_path, "r") as file:  # Opens the file containing the solution
        for line in file:  # Reads each line of the file
            region, color = line.strip().split(" -> Color ")  # Splits the region and assigned color
            colors[region] = int(color)  # Stores the color as an integer in the dictionary
    return colors  # Returns the dictionary of assigned colors


def read_graph(file_path):
    """Reads the map and returns a NetworkX graph representing the regions and their adjacency relationships."""
    G = nx.Graph()  # Initializes an undirected graph
    with open(file_path, "r") as file:  # Opens the file containing the graph definition
        for line in file:  # Reads each line of the file
            parts = line.strip().split("(")  # Splits the line at the first parenthesis
            if len(parts) > 1:
                args = parts[1].replace(").", "").split(",")  # Cleans up the line and extracts the arguments
                args = [arg.strip() for arg in args]  # Removes unnecessary spaces
                if "region" in parts[0]:  # Checks if the line defines a region
                    G.add_node(args[0])  # Adds the region as a node in the graph
                elif "adjacent" in parts[0]:  # Checks if the line defines an adjacency relationship
                    G.add_edge(args[0], args[1])  # Adds an edge connecting the two regions
    return G  # Returns the NetworkX graph object


def plot_graph(graph_file, solution_file):
    """Displays the colored graph using Matplotlib based on the found solutions."""
    G = read_graph(graph_file)  # Reads the graph from the file
    colors_map = {1: "red", 2: "blue", 3: "green", 4: "yellow"}  # Dictionary mapping color numbers to actual colors
    solution = read_solution(solution_file)  # Reads the coloring solution from the file

    node_colors = [colors_map[solution[node]] for node in G.nodes()]  # Assigns each node the corresponding color

    plt.figure(figsize=(8, 6))  # Sets the figure size for display
    pos = nx.spring_layout(G, seed=42)  # Generates a node layout for display
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=800, edge_color="black", font_size=10, font_weight="bold")  # Draws the graph

    plt.title("Graph Coloring")  # Adds a title to the display
    plt.show()  # Displays the colored graph
