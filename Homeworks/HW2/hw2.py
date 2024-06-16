
"""
CS161: Homework 2
Preyasi Gaur
705704939

Discussed with: Nitya Khanna, Anmol Gupta

Question 1
The function processes the tree nodes arranged as visited in a left-to-right breadth-first-search. We begin by initialising a queue and a variable to store the answer. Next, we check if the tree is not a tuple, and if it not, we just return the tree. If it is a tuple, then we use a for loop to append the elements of the tuple to the queue. We pop the elements one by one and check if the element is a tuple. If the popped element is a tuple we again append it to the queue. If it is not a tuple then we append it to the answer. Thus, it ends up returning the tree nodes arranged as visited in a left-to-right Breadth First Search

Question 2
The function processes tree nodes arranged as visited in a left-to-right depth-first-search. We begin by initialising a stack and a variable to store the answer. Just like in Question 1, we check if the input is not a tuple, in which case we just return the input as a tuple. If it is a tuple, then we run a for loop and append the elements of the tuple to the stack. Next, we check if the stack is non empty, we pop the elements of the stack. I gf the popped element is a tuple, we append the elements of the tuple to the stack using a for loop. If the popped element is not a tuple, then we just append it to the answer. Finally, to get the left-to-right depth-first-search, we reverse the answer tuple. 

Question 3
The set of functions helps process a given tree as a tuple of leaf nodes in the order they are visited by a right-to-left depth-first iterative-deepening search. The depth_limited_search function performs a right-to-left depth-first search (DFS) on a nested tuple representing a tree, processing nodes only up to a specified depth limit. If the current node is a leaf and within the depth limit, it's returned; otherwise, if it's an internal node at the depth limit, the function halts further recursion and returns an empty tuple. Building upon this, the DFID function utilizes iterative deepening, applying depth_limited_search repeatedly with increasing depth limits from 0 up to D. This technique combines the advantages of DFS's space efficiency with the completeness of breadth-first search (BFS), ensuring that all nodes are explored systematically and revisited at each depth level, accumulating the nodes in a tuple that records their order of visitation for each iterative depth.

Question 4
• FINAL_STATE(S): Checks if the given state S matches the goal state (True, True, True, True), returning True if it does, otherwise False.

• NEXT_STATE(S, A): Calculates the next state by moving Homer alone or with one of the entities (baby, dog, or poison) based on the action A, ensuring that the move doesn't lead to an unsupervised situation or is not possible due to location mismatches, and returns a list containing the resulting state tuple or an empty list for invalid moves.

• SUCC_FN(S): Generates all possible successor states from the current state S by applying all valid movements (Homer alone or with an entity), and compiles these states into a list if they are valid.

• ON_PATH(S, STATES): Determines if the current state S is already included in the list of states STATES visited during the depth-first search, returning True if it is, which helps prevent cycles in the search path.

• MULT_DFS(STATES, PATH): Performs a depth-first search on each state in the list STATES, appending the current path PATH, and returns the complete path to the goal state if one of these searches succeeds, otherwise returns an empty list if none reach the goal.

• DFS_SOL(S, PATH): Conducts a depth-first search from state S, using PATH to track the visited nodes; checks if S is the goal state or already on the PATH to prevent revisits, and leverages MULT_DFS for further exploration, returning the path to the goal state if found, or an empty list otherwise.


"""

#Question 1

#Arguments:
    #TREE (tuple): A nested tuple structure representing a tree. Elements within this structure can be of anything, as well as further tuples.
#Returns:
    #Tuple: The tuple of the tree nodes arranged as visited in a left to right BFS search.
def BFS(TREE):
  queue_ans = []
  ans = ()
  if (type(TREE) is not tuple):
      return (TREE, )

  for i in TREE:
      queue_ans.append(i)

  while (len(queue_ans) > 0):
      element = queue_ans.pop(0)

      if (type(element) is tuple):
          for i in element:
              queue_ans.append(i)
      else:
        ans += (element, )
  return ans


#Question 2

#Arguments:
    #TREE (tuple): A nested tuple structure representing a tree. Elements within this structure can be of anything, as well as further tuples.
#Returns:
    #Tuple: The tuple of the tree nodes arranged as visited in a left-to-right depth-first search.

def DFS(TREE):
  stack_ans = []
  ans = ()

  if(type(TREE) is not tuple):
      return (TREE, )

  for i in TREE:
      stack_ans.append(i)

  while(len(stack_ans) > 0):
      element = stack_ans.pop()
      if(type(element) is tuple):
          for j in element:
              stack_ans.append(j)
      else:
          ans += (element, )  # Note the comma to make it a tuple
  return ans[::-1]


#Question 3

#Arguments:
    #tree (tuple): A nested tuple structure representing a tree. Elements within this structure can be of anything, as well as further tuples.
    #limit (int): specifying the limit till which depth we want to go
    #depth (int): the current depth of recursion or search in the tree, used internally to track the depth at recursion.
#Returns:
    #Tuple: all the leaf nodes found within the depth limit for this subtree processed in a right-to-left order

def depth_limited_search(tree, limit, depth=0):
    if type(tree) is not tuple:
        if depth <= limit:
            return (tree, )
        else:
            return ()
    else:
        if depth >= limit:
          return ()

        result = ()
        for child in reversed(tree):
            result += depth_limited_search(child, limit, depth + 1)
        return result

#Arguments:
    #TREE (tuple): A nested tuple structure representing a tree. Elements within this structure can be of anything, as well as further tuples.
    #D (int): maximum depth limit for the iterative deepening process
#Returns:
    #Tuple: all the leaf nodes found within the depth limit for this subtree processed in a right-to-left order

def DFID(TREE, D):
    result = ()
    for depth in range(D + 1):
        result += depth_limited_search(TREE, depth)
    return result


#Question 4

# First, we define the helper functions of DFS_SOL.

# FINAL_STATE takes a single argument S, the current state, and returns True if it
# is the goal state (True, True, True, True) and False otherwise.

#Arguments: 
    #S: tuple containing the state 
#Returns: 
    #Boolean True/False: depending on if the state is the final state 
def FINAL_STATE(S):
    if S == (True, True, True, True):
        return True
    else: 
        return False


# NEXT_STATE returns the state that results from applying an operator to the
# current state. It takes two arguments: the current state (S), and which entity
# to move (A, equal to "h" for homer only, "b" for homer with baby, "d" for homer
# with dog, and "p" for homer with poison).
# It returns a list containing the state that results from that move.
# If applying this operator results in an invalid state (because the dog and baby,
# or poisoin and baby are left unsupervised on one side of the river), or when the
# action is impossible (homer is not on the same side as the entity) it returns [].
# NOTE that NEXT_STATE returns a list containing the successor state (which is
# itself a tuple)# the return should look something like [(False, False, True, True)].

#Arguments: 
    #S: tuple containing the state 
    #A: the entity which is to move
#Returns: 
    #list: list containing a tuple of the successor state or an empty list if the move is invalid.
def NEXT_STATE(S, A): 
    ans=()
    homer, baby, dog, poison = S

    if A == 'h' and ((baby == homer and dog == homer and baby != poison) or (baby == homer and poison == homer and baby != dog)):
        return []  
    if A == 'b' and homer != baby:
        return []
    if A == 'd' and homer != dog:
        return []
    if A == 'p' and homer != poison:
        return []
    
    if A == 'h':
        ans = (not homer, baby, dog, poison)
    elif A == 'b':
        ans = (not homer, not baby, dog, poison)
    elif A == 'd':
        ans = (not homer, baby, not dog, poison)
    elif A == 'p':
        ans = (not homer, baby, dog, not poison)
    
    new_homer, new_baby, new_dog, new_poison = ans
    if (new_baby == new_dog and new_baby != new_homer) or (new_baby == new_poison and new_baby != new_homer):
        return []  

    return [ans]

# SUCC_FN returns all of the possible legal successor states to the current
# state. It takes a single argument (S), which encodes the current state, and
# returns a list of each state that can be reached by applying legal operators
# to the current state.

#Arguments: 
    #S: tuple contaiing current state
#Returns: 
    #list: containg every state that can be reached by using legal operators to S
def SUCC_FN(S):
    ans = []
    acts = ['h', 'b', 'd', 'p']
    for i in acts:
        ans += NEXT_STATE(S, i)
    return ans


# ON_PATH checks whether the current state is on the stack of states visited by
# this depth-first search. It takes two arguments: the current state (S) and the
# stack of states visited by DFS (STATES). It returns True if S is a member of
# STATES and False otherwise.

#Arguments: 
    #S: tuple containing the current state
    #STATES: stack of states visited by DFS(STATES)
#Returns:
    #Boolean True/False: depending on whether S is a member of STATES 
def ON_PATH(S, STATES):
    if S in STATES: 
        return True
    else: 
        return False


# MULT_DFS is a helper function for DFS_SOL. It takes two arguments: a list of
# states from the initial state to the current state (PATH), and the legal
# successor states to the last, current state in the PATH (STATES). PATH is a
# first-in first-out list of states# that is, the first element is the initial
# state for the current search and the last element is the most recent state
# explored. MULT_DFS does a depth-first search on each element of STATES in
# turn. If any of those searches reaches the final state, MULT_DFS returns the
# complete path from the initial state to the goal state. Otherwise, it returns
# [].
#Arguments: 
    #PATH: list of states from the initial state to the current state
    #STATES: the legal successor states to the last, current state in the PATH 
#Returns: 
    #list: the complete path from the initial to the goal state
def MULT_DFS(STATES, PATH):
    for i in STATES:
        multAns = DFS_SOL(i, PATH)
        if(len(multAns) != 0):
            return multAns

    return []

# DFS_SOL does a depth first search from a given state to the goal state. It
# takes two arguments: a state (S) and the path from the initial state to S
# (PATH). If S is the initial state in our search, PATH is set to []. DFS_SOL
# performs a depth-first search starting at the given state. It returns the path
# from the initial state to the goal state, if any, or [] otherwise. DFS_SOL is
# responsible for checking if S is already the goal state, as well as for
# ensuring that the depth-first search does not revisit a node already on the
# search path (i.e., S is not on PATH).

#Arguments: 
    #S: a tuple containing the state
    #PATH: path from the initial state to S 
#Returns: 
    #list: the path from the initial state to the goal state if one is found; otherwise, it returns an empty list if no path exists
def DFS_SOL(S, PATH):
    if (FINAL_STATE(S) == True):
        return PATH + [S]

    if (ON_PATH(S, PATH)):
        return []

    return MULT_DFS
