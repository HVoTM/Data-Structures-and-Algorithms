
"""
A trie (pronounced as "try") or prefix tree (or digital tree) is a tree data structure used to efficiently store and retrieve keys \
in a dataset of strings. 
There are various applications of this data structure, such as autocomplete, spellcheckers, IP routing.
Further documentation: https://en.wikipedia.org/wiki/Trie

Common string-searching algorithms: predictive text, approximate string matching, spell checking
"""
from typing import Self

class TrieNode:
    # Initilization step
    def __init__(self):
        self.children = [None] * 26 # representing the alphabets
        # NOTE: in special case, if ASCII encoding is used, we will initialize to 256 elements in the children array
        # https://en.wikipedia.org/wiki/ASCII
        # Sentinel value to indicate if we reach the end of word
        self.isTerminal = False 
        # Optional value: which is associated with each key stored in the last character of string
        self.Value = None

    def insert(self, word: str) -> None:
        # Starting with the root Trie node, we insert the first character
        curr = self
        # Iterate the characters in the word
        for ch in word:
            # Check if the node exists for the current character in the Trie
            # ord() is a built-in function that can translate the character into unicode representation of the ASCII 
            index = ord(ch) - ord('a')
            if curr.children[index] is None:
                
                # If the node for the current character does not exist, we make a new node
                newNode = TrieNode()
                # Keep the reference for the newly created node
                curr.children[index] = newNode
            
            # Move the curr pointer to the new Node that we have made 
            curr = curr.children[index]
        # Mark the end of the word
        curr.isTerminal = True

    def search(self, word: str) -> bool:
        # Initialize the curr pointer with the root note
        curr = self
        # Iterate across the length of the input word
        for ch in word:
            # Check if the node exists for the current character in the Trie
            index = ord(ch) - ord('a')
            if curr.children[index] is None:
                return False
            # Move the node to the laready existing node for the existing character
            curr = curr.children[index]
        # Return true if the word exists and is marked as ending
        return curr.isTerminal

    def startsWith(self, prefix: str) -> bool:
        # Initialize the pointer
        curr = self
        # Iterate over the characters of the input prefix
        for ch in prefix:
            # Check if the node exists in the current Trie Node for the current character 
            index = ord(ch) - ord('a')
            if curr.children[index] is None:
                return False
            # If it is True, move the node to the already existing node
            curr = curr.children[index]
        return True
    
    def delete(self, word:str) -> Self: # or we can use "TrieNode" - https://stackoverflow.com/questions/33533148/how-do-i-type-hint-a-method-with-the-type-of-the-enclosing-class
        curr = self
        if word is None: 
            if curr.isTerminal == True:
                curr.isTerminal = False
                # self.Value = None
            
            for i in range(curr.children):
                if curr.children[i] is not None:
                    return curr
                
            return None
        self.children[word[0]] = self.delete(self.children[word[0]], word[1:])

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)