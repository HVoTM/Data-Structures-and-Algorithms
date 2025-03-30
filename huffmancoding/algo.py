# Huffman Coding Algorithm Implementation
# https://en.wikipedia.org/wiki/Huffman_coding
# https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/

import heapq

class node:
    # init a huffman tree
    def __init__(self, freq, symbol, left=None, right=None) -> None:
        # frequency of symbol
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right

        # tree direction  (0/1)
        self.huff = ' '

    def __lt__ ():
        pass

def printNodes(node, val =''):
    pass
    #