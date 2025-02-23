# LEETCODE 208. Implement Trie (Prefix Tree)
# Topic: Trie, Hash Table, String, Design, Tree

class Trie:

    def __init__(self):
        self.children = [None] * 26 # representing the alphabets
        self.isTerminal = False # a boolean sentinel to mark if we reach the end of word

    def insert(self, word: str) -> None:
        curr = self
        # Iterate the characters in the word
        for ch in word:
            # Check if the node exists for the current character in the Trie
            index = ord(ch) - ord('a')
            if curr.children[index] is None:
                
                # If the node for the current character does not exist, we make a new node
                newNode = Trie()
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
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)