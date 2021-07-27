import unicodedata
import re
import json

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import pandas as pd
import acquire as aq

def basic_clean(word):
    '''
    This function takes in a string and applies basic text cleaning to it. 
    It lower cases everything, normalizes unicode characters and removes any character that is not a 
    letter, number, whitespace or a single quote. 
    '''
    word = word.lower()
    word = unicodedata.normalize('NFKD', word)\
    .encode('ascii', 'ignore')\
    .decode('utf-8')
    word = re.sub(r"[^a-z0-9'\s]", '', word)
    return word

def tokenize(string):
    '''
    This function takes in a string and tokenizes all the words in the string.
    It then returns the tokenized string.
    '''
    # Create the tokenizer
    tokenizer = nltk.tokenize.ToktokTokenizer()
    # Use the tokenizer
    tokenized_string = tokenizer.tokenize(string, return_str = True)
    return tokenized_string

def stem(text):
    '''
    This function takes in some text and returns the text after applying stemming to all the words.
    '''
    # Create porter stemmer.
    ps = nltk.porter.PorterStemmer()
    stems = [ps.stem(word) for word in text.split()]
    # Join our lists of words into a string again; assign to a variable to save changes
    text_stemmed = ' '.join(stems)
    return text_stemmed

def lemmatize(text):
    '''
    This function takes in some text and returns the text after applying lemmatization to all the words.
    '''
    # Create the Lemmatizer.
    wnl = nltk.stem.WordNetLemmatizer()
    lemms = [wnl.lemmatize(word) for word in text.split()]
    # Join our list of words into a string again; assign to a variable to save changes.
    text_lemmatized = ' '.join(lemms)
    return text_lemmatized

def remove_stopwords(text, extra_words = [], exclude_words = []):
    '''
    This function takes in some text, optional extra_words and exclude_words parameters
    with default empty lists and returns the text after removing all stop words.
    '''
    # Create stopword_list
    stopword_list = stopwords.words('english')
    
    # Remove 'exclude_words' from stopword_list to keep these in my text.
    stopword_list = set(stopword_list) - set(exclude_words)
    
    # Add in 'extra_words' to stopword_list
    stopword_list = stopword_list.union(set(extra_words))
    
    # Split words in string.
    words = text.split()
    
    # Create a list of words from my string with stopwords removed and assign to variable.
    filtered_words = [word for word in words if word not in stopword_list]
    
    # Join words in the list back into strings and assign to a variable.
    string_without_stopwords = ' '.join(filtered_words)
    
    return string_without_stopwords
    

