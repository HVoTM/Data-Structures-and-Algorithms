# Trees
A hiearchical structure that is used to represent and organize data for easier navigation and search, instead of a linear run like an array.

# Properties
Consists of nodes, the topmost one is called a root, the nodes below are the child nodes. All the nodes are connected by edges and have a hierarchical relationship between themselves.
- Number of edges
- Depth
- Height of a node
- Height of the Tree
- Degree of a node

## Terminologies:
- Parent nodes
- Child nodes
- Root node
- Leaf nodes
- Ancestor - Descendant
- Siblings, Neighbors, Grandparents - Grandchildren, 
- Level
- External, Internal, Central, Structural
- Subtree

# Basic Operations:
- Create – create a tree in the data structure.
- Insert − Inserts data in a tree.
- Search − Searches specific data in a tree to check whether it is present or not.
- Remove
- Traversal:
    + Preorder Traversal – perform Traveling a tree in a pre-order manner in the data structure.
    + In order Traversal – perform Traveling a tree in an in-order manner.
    + Post-order Traversal –perform Traveling a tree in a post-order manner.

# Application:
- File System:  This allows for efficient navigation and organization of files.
- Data Compression: Huffman coding is a popular technique for data compression that involves constructing a binary tree where the leaves represent characters and their frequency of occurrence. The resulting tree is used to encode the data in a way that minimizes the amount of storage required.
- Compiler Design: In compiler design, a syntax tree is used to represent the structure of a program. 
- Database Indexing: B-trees and other tree structures are used in database indexing to efficiently search for and retrieve data. 
- Natural Language Processing

# Mathematical Properties of Trees

## Number of edges vs. number of nodes in a tree
Let m be the number of edges and n number of nodes
$$ 
m = n - 1
$$

## Lower bound on Depth of a Binary Tree
Proposition: 
Every binary tree with n nodes has depth d at least
$$\lfloor log_{2}{n}\rfloor$$

## 2-tree(binary tree)
> Is a tree where every node that is not a leaf has exactly two children

L(T) and I(T): number of leaf and internal nodes of a tree. Let $L=L(T),I = I(T)$

Proposition: Let T be a 2-tree. Then $L = I + 1$
- Corollary 1: $n=2.I +1$
- Corollary 2: $n=2.L-1$

## Lower bound on depth of a binary tree in terms of number of leaf nodes
Every binary tree with L leaf nodes has depth d at least
$$\lceil log_{2}L\rceil$$
Equality is achieved for a complete binary tree.

