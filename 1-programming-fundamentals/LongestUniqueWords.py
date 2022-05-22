# Write a function that accepts a list of strings that represent words and a positive integer n, representing the number of words to return.
# Your function should return a new list containing the n longest unique words from the input list. Words are unique if they appear one time in the input list.

def get_n_longest_unique_words(words, n):
    unique_words = get_unique_words(words)
    sorted_words = sorted(unique_words, reverse=True, key=len)
    return sorted_words[:n]

def get_unique_words(words):
    unique_words = []
    for word in words:
        if words.count(word) == 1:
            unique_words.append(word)

    return unique_words