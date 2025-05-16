def is_anagram(word1, word2):
    # Sort the letters of both words
    # For example, "cat" becomes ['a', 'c', 't']
    # and "tac" also becomes ['a', 'c', 't']
    return sorted(word1) == sorted(word2)

# Test the function
print(is_anagram("cat", "tac"))  # True, because both have same letters
