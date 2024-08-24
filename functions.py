import pandas as pd
import string

def get_unique_list_f(lst):
    """
    Takes a list as an argument and returns a new list with unique elements from the first list.

    Parameters:
    lst (list): The input list.

    Returns:
    list: A new list with unique elements from the input list.
    """
    
    get_unique = list(dict.fromkeys(lst)) # dict.fromkeys --> creates a dictionary {1: None, 2:None, etc}. 
                                          # list --> convers the dictionary bact to a list

    return get_unique

def count_case_f(string):
    """
    Returns the number of uppercase and lowercase letters in the given string.

    Parameters:
    string (str): The string to count uppercase and lowercase letters in.

    Returns:
    A tuple containing the count of uppercase and lowercase letters in the string.
    """
    
    uppercase_count = sum(1 for char in string if char.isupper())
    lowercase_count = sum(1 for char in string if char.islower())

    print(f"Uppercase count: {uppercase_count}, Lowercase count: {lowercase_count}")

def remove_punctuation_f(sentence):
    """
    Removes all punctuation marks (commas, periods, exclamation marks, question marks) from a sentence.

    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    str: The sentence without any punctuation marks.
    """

    # remove punctuation
    translator = str.maketrans("","", string.punctuation)
    sentence_cleaned = sentence.translate(translator).lower()

    return sentence_cleaned

def word_count_f(sentence):
    """
    Counts the number of words in a given sentence. To do this properly, first it removes punctuation from the sentence.
    Note: A word is defined as a sequence of characters separated by spaces. We can assume that there will be no leading or trailing spaces in the input sentence.
    
    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    int: The number of words in the sentence.
    """
    words = remove_punctuation_f(sentence).split()
    number_of_words = len(words)

    return number_of_words