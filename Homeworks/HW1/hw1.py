"""
CS161: Homework 1
Preyasi Gaur 
705704939 
Discussed With: Anmol Gupta, Sahiti Gabrani


Question 1 
The function computes the Nth term of a modified Pandovan sequence using memoization.
We declare the base cases in the dict, PAD(0) = PAD(1) = PAD(2) = 1 and for N > 2, we use the recurrence relation PAD(N) = PAD(N-2) + PAD(N-3), and store the value in the memo.

Question 2
The function computes the number of sums required to calculare the Pandovan of the Nth number.
We declare that for the base cases(N <= 2), the SUMS function return 0, as they are already provided. For all N > 2, we define the recurrence relation 1 + SUMS(N-2) + SUMS(N-3), and return.

Question 3
The fuction recursively replaces all elements in a nested tuple structure with a '?'.
We take a tree represented as nested tuples. We recursively traverse the whole tree and replace each node with '?', while preserving the structure of the tree. 

Question 4
The fuction recursively calculates the height of the tree. 
We take a tree represented as nested tuples. We, then, check if the input is not a tuple, if not, we returns 0, else we call the function on every subtree and takes the maximum of that and adds 1 to calculate the maximum height. 

Question 5
The function recursively returns the post order traversal of a given tree. 
We take a tree represented as nested tuples. Next, we check if the given node is not a tuple, if it is not then we return the node value. Else, we recursively call the function of the Left subtree, Right subtree and the node, to return the post order traversal. 

"""

#Question 1

#Arguments: 
    #N (int): The position in the sequence for which to compute the value
#Returns: 
    #int: The value of the Nth term in the sequence]
def PAD(N):
  if 'memo' not in PAD.__dict__:
      PAD.memo = {0: 1, 1: 1, 2: 1}
  if N in PAD.memo:
      return PAD.memo[N]

  PAD.memo[N] = PAD(N-2) + PAD(N-3)

  return PAD.memo[N]


#Question 2

#Arguments:
    #N (int): The position in the sequence for which to compute the number of sums required.
#Returns:
    #int: The number of sums required for the Nth term in the sequence.
def SUMS(N):
  if N <= 2:
      return 0
  else:
      return 1 + SUMS(N-2) + SUMS(N-3)


#Question 3

#Arguments:
    #TREE (tuple): A nested tuple structure representing a tree. Elements within this structure can be of anything, as well as further tuples.
#Returns:
    #tuple: A nested tuple of the same structure but with all elements being '?'.
def ANON(TREE):
  if type(TREE) is not tuple:
    return '?'
  else:
    return tuple(ANON(sub) for sub in TREE)


#Question 4

#Arguments:
    #TREE (tuple): A nested tuple structure representing a tree. Elements within this structure can be of anything, as well as further tuples.
#Returns:
    #int: The height of the tree.
def TREE_HEIGHT(TREE):
  if type(TREE) is not tuple:
    return 0
  else:
    return 1 + max(TREE_HEIGHT(subtree) for subtree in TREE)


#Question 5

#Arguments:
    #TREE (tuple): A nested tuple structure representing a tree. Elements within this structure can be of anything, as well as further tuples.
#Returns: 
    #tuple: the postorder traversal of the numbers in TREE.
def TREE_ORDER(TREE):
  if type(TREE) != tuple:
     return (TREE,)
  else:
    L, m, R = TREE
    return TREE_ORDER(L) + TREE_ORDER(R) + (m,)
