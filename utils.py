import os

def load_words(filename):
    """
    Loads a list of words from a given file.
    Assumes the file is in the 'data' subdirectory.
    """
    filepath = os.path.join('data', filename)
    try:
        with open(filepath, 'r') as f:
            # Read all lines, strip whitespace/newlines from each,
            # and filter out any empty lines.
            words = [line.strip() for line in f if line.strip()]
        return words
    except FileNotFoundError:
        print(f"Error: Word file not found at '{filepath}'")
        return []

def to_leet_speak(text):
    """Converts a string to basic leet speak."""
    leet_map = {
        'a': '4', 'e': '3', 'g': '6', 'i': '1',
        'o': '0', 's': '5', 't': '7',
    }
    # We iterate through the map, not the text, for efficiency
    for char, leet_char in leet_map.items():
        text = text.replace(char, leet_char)
    return text