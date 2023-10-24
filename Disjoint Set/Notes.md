Optimization of the Disjoint Set can be implemented using Union by Rank/Size and Path Compression

1. Union by Rank:
    - Considers height of the tree as the factor
2. Union by Size: 
    - Considers size of the tree as the factor while attaching one tree to the other  
3. Find with Path Compression: O(log n)
    - It speeds up the data structure by compressing the height of the trees. It can be achieved by inserting a 
small caching mechanism into the Find operation. 

The total time complexity is:
$O(\alpha (n))$
where $\alpha(n)$ is the inverse Ackermann function, which grows very steadily

Space complexity: O(n) 