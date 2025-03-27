:- module(graph_coloring, [color_graph_clp/3, color_graph_clp_mrv/3]).
:- use_module(library(clpfd)).

% Apply constraints between adjacent regions: two adjacent regions must have different colors
apply_constraints(_, [], _).  % Base case: if the adjacency list is empty, nothing to apply
apply_constraints(Regions, [(R1, R2) | AdjRest], Coloring) :-
    nth0(Index1, Regions, R1), % Find the index of region R1 in the list of regions
    nth0(Index2, Regions, R2), % Find the index of region R2 in the list of regions
    nth0(Index1, Coloring, C1), % Retrieve the color assigned to R1
    nth0(Index2, Coloring, C2), % Retrieve the color assigned to R2
    C1 #\= C2, % Constrain the colors to be different
    apply_constraints(Regions, AdjRest, Coloring). % Recursively apply constraints to other adjacencies

% CLP(FD) Algorithm using the First-Fail (FF) strategy
color_graph_clp(Regions, Adjacencies, Coloring) :-
    statistics(runtime, [Start|_]), % Start measuring execution time
    length(Regions, N), % Determine the number of regions
    length(Coloring, N), % Create a list of variables of the same length as the number of regions
    Coloring ins 1..4, % Restrict colors to be between 1 and 4
    apply_constraints(Regions, Adjacencies, Coloring), % Apply adjacency constraints
    labeling([ff], Coloring), % Use First-Fail strategy (choosing the most constrained variables first)
    statistics(runtime, [End|_]), % Stop measuring execution time
    Time is End - Start, % Calculate total execution time
    format('Execution time CLP(FD): ~w ms\n', [Time]). % Display execution time

% CLP(FD) Algorithm with Minimum Remaining Values (MRV)
color_graph_clp_mrv(Regions, Adjacencies, Coloring) :-
    statistics(runtime, [Start|_]),  % Start measuring execution time
    length(Regions, N), % Determine the number of regions
    length(Coloring, N), % Create a list of variables of the same length as the number of regions
    Coloring ins 1..4, % Restrict colors to be between 1 and 4
    apply_constraints(Regions, Adjacencies, Coloring), % Apply adjacency constraints
    labeling([min], Coloring), % Use MRV strategy (choosing variables with the least options first)
    statistics(runtime, [End|_]), % Stop measuring execution time
    Time is End - Start, % Calculate total execution time
    format('Execution time CLP(FD) + MRV: ~w ms\n', [Time]). % Display execution time
