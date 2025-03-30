# 151. Reverse Words in a String
# Given an input string, reverse the string word by word.
#
# Topic: String, array

class Solution:
    def reverseWords(self, s: str) -> str:
        # Initialize a list to store the words
        words = []
        # Making a flag to signal if the current character is in a word or is it a start of a new word
        next_word = True
        # Index value for the array for words
        i = 0
        # Pass through the string 
        for character in s:
            if character.isalnum() and next_word:
                next_word = False
                # append the new word's first character
                words.append(character)

            elif character.isalnum() and not next_word:
                # concatenate the current word with its respective characters
                words[i] += character

            # signifying end of this word and move onto the next one, increment i counter
            elif character == ' ' and not next_word:
                next_word = True
                i += 1
            # For when we keep encountering whitespaces
            elif character == ' ' and next_word:
                continue
        # Initialize an empty array to add the words to
        revers = ''
        for i in range(len(words) - 1):
            revers += words.pop() + ' '
        return revers + words.pop()   
