# Write a function that accepts a string and returns the caesar cipher encoding of that string according to a secondary input parameter named offset.

def caesar_cipher(string, offset):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    encoded_string = ""

    for char in string:
      char_idx = alphabet.index(char)
      offset_idx = char_idx - offset
      encoded_string += alphabet[offset_idx]

    return encoded_string