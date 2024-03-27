import re

def extract_quotes(input_string):
    """
    Extracts substrings enclosed in double quotes from the given input string.

    Args:
        input_string (str): The string from which to extract quotes.

    Returns:
        list: A list containing all substrings found within double quotes.
    """
    # This pattern matches any sequence of characters enclosed in double quotes
    # The ?: tells Python not to capture the quotes themselves as a group
    pattern = r'"(.*?)"'
    
    # re.findall() finds all the substrings where the pattern matches, and returns them as a list
    quotes = re.findall(pattern, input_string)
    
    return quotes

# print(extract_quotes('asldfkjasdf "fwoiuewioejf" asdfasdf'))