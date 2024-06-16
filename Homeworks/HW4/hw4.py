##############
# Homework 4 #
##############

"""
Preyasi Gaur 
705704939
Discussed with: Nitya Khanna, Anmol Gupta 

1. def node2var(n, c, k): The index of the variable is calculated by multiplying the node index n with the number of possible colors k and adding the color number c. 

2. def at_least_one_color(n, k): We iterate over each color from 1 to k. For each color, we add the corresponding Boolean variable for node n to the clause. The clause is represented as a list of tuples, where each tuple contains a single variable. If any of these variables is true (i.e., the node is assigned that color), the constraint is satisfied.

3. def at_most_one_color(n, k): We iterate over all pairs of colors (color1, color2) where c1 < c2. For each pair, we create a clause that includes the negation of the Boolean variables representing node n being assigned colors c1 and c2. The clause ensures that at most one of these variables can be true, satisfying the constraint that the node gets at most one color.

4. def generate_node_clauses(n, k): We first call the at_least_one_color function to generate the clause ensuring that the node gets at least one color. Then, we call the at_most_one_color function to generate the clause ensuring that the node gets at most one color. Lastly, we combine both sets of clauses and return the result.

5. def generate_edge_clauses(e, k): We take an edge represented by a tuple, e and the number of possible colors k. It then creates a list of clauses representing the constraint that nodes connected by the edge e cannot have the same color. Each clause in the list ensures that if nodes node1 and node2 connected by the edge e are assigned the same color i, it leads to a contradiction. Finally, it returns the list of clauses.
"""

# Exercise: Fill this function.
# Returns the index of the variable that corresponds to the fact that
# "Node n gets Color c" when there are k possible colors

#Arguments: 
    # n (int): Node index
    # c (int): Color number
    # k (int): Number of possible colors
# Returns:
    # int: Index of the variable
def node2var(n, c, k):
    return (n - 1) * k + c 

# Exercise: Fill this function
# Returns *a clause* for the constraint:
# "Node n gets at least one color from the set {1, 2, ..., k}"

# Arguments:
#     n (int): Node index
#     k (int): Number of possible colors
# Returns:
#     list of tuples: Clause representing the constraint
def at_least_one_color(n, k):
    at_least_one_color_clause = []
    for color in range(1,k+1):
        at_least_one_color_clause.append(node2var(n, color, k))   
    return at_least_one_color_clause

# Exercise: Fill this function
# Returns *a list of clauses* for the constraint:
# "Node n gets at most one color from the set {1, 2, ..., k}"

# Arguments:
#     n (int): Node index
#     k (int): Number of possible colors
# Returns:
#     list of tuples: Clause representing the constraint
def at_most_one_color(n, k):
    at_most_one_color_clause = []
    for color1 in range(1, k + 1): 
        for color2 in range(1, color1):
            at_most_one_color_clause.append([- node2var(n, color1, k), - node2var(n, color2, k)])  #Applying De Morgan's Law
    return at_most_one_color_clause

# Exercise: Fill this function
# Returns *a list of clauses* for the constraint:
# "Node n gets exactly one color from the set {1, 2, ..., k}"

# Arguments:
#     n (int): Node index
#     k (int): Number of possible colors
# Returns:
#     list of lists: List of clauses
def generate_node_clauses(n, k):
    generate_node_clauses_list = at_most_one_color(n, k)
    generate_node_clauses_list.append(at_least_one_color(n, k))
    return generate_node_clauses_list 

# Exercise: Fill this function
# Returns *a list of clauses* for the constraint:
# "Nodes connected by an edge e (represented by a list)
# cannot have the same color"

# Arguments:
#     e (tuple): Edge represented by a tuple of two node indices.
#     k (int): Number of possible colors.
# Returns:
#     list of lists: List of clauses.
def generate_edge_clauses(e, k):
    node1,node2 = e
    ans_clause = []
    for i in range(1, k + 1):
        ans_clause.append([-node2var(node1, i, k), -node2var(node2, i, k)])
    return ans_clause

# The function below converts a graph coloring problem to SAT
# Return CNF as a list of clauses
# DO NOT MODIFY
def graph_coloring_to_sat(graph_fl, sat_fl, k):
    clauses = []
    with open(graph_fl) as graph_fp:
        node_count, edge_count = tuple(map(int, graph_fp.readline().split()))
        for n in range(1, node_count + 1):
            clauses += generate_node_clauses(n, k)
        for _ in range(edge_count):
            e = tuple(map(int, graph_fp.readline().split()))
            clauses += generate_edge_clauses(e, k)
    var_count = node_count * k
    clause_count = len(clauses)
    with open(sat_fl, 'w') as sat_fp:
        sat_fp.write("p cnf %d %d\n" % (var_count, clause_count))
        for clause in clauses:
            sat_fp.write(" ".join(map(str, clause)) + " 0\n")
    return clauses, var_count

# Example function call
if __name__ == "__main__":
    graph_coloring_to_sat("graph1.txt", "graph1_3.cnf", 3)