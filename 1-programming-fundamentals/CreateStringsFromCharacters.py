# Write a function that accepts a dictionary of characters (keys) and integers (values) as frequencies and two strings as input. The function should return:
# - 2 if there are sufficient characters to create both strings without reusing chars
# - 1 if there are sufficient characters to create either string1 or string2 without reusing chars
# - 0 if there are not sufficient characters to create any of the strings

def create_strings_from_characters(frequencies, string1, string2):
    can_create_string1 = can_create_string_from_frequencies(
        frequencies, string1)
    can_create_string2 = can_create_string_from_frequencies(
        frequencies, string2)

    if (not can_create_string1) or (not can_create_string2):
        if can_create_string1 or can_create_string2:
            return 1

        return 0

    for character in string1 + string2:
        if character not in frequencies or frequencies[character] == 0:
            return 1

        frequencies[character] -= 1

    return 2


def can_create_string_from_frequencies(frequencies, string):
    for character in set(string):
        if string.count(character) > frequencies.get(character, 0):
            return False

    return True