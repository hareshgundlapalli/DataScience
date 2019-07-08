#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys


# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

def return_hash(filename):
    # this function is common between two functions to open the file and
    # load it into the dict
    words = {}
    f = open(filename, 'rU')
    # Convert the whole file to a single string and store it in lower case
    text = f.read().lower()
    # Split the whole string to individual words and string1 becomes the list
    wordslist = text.split()
    # Loop in all the entries of the list to store the count of each item
    for i in wordslist:
        words[i] = text.count(i)
    # Close the file
    f.close()
    # Return the dict to individual function when called
    return words


def print_words(filename):
    # call the hash function above by passing the file and returning the hash
    # table
    words = return_hash(filename)
    # Sort the entries in Hash table and for each entry display the key and
    # value
    for k in sorted(words.keys()):
        if words[k] == 1:
            print ('Word:', '\'', k, '\'', 'occured', words[k], 'time.')
        else:
            print ('Word:', '\'', k, '\'', 'occured', words[k], 'times.')


###
# function used to return the second entry for custom sort on top count.
# If you use tuple as in List1 program, then use -1 to return the last item.
def func(x):
    return x[-1]  # or return x[1] since we already know there are 2 entries in each tuple


def print_top(filename):
    # call the hash function above by passing the file and returning the hash
    # table
    words = return_hash(filename)
    # Custom sort on Dict where the second item is returned from each tuple and
    # is sorted in reverse order.
    items = sorted(words.items(), key=func, reverse=True)
    # This is tricky and i forgot. for each entry till 20 count, display key
    # and the value of the dict to display top 20 entries.
    for i in items[:20]:
        print(i[0], i[1])


def print_last(filename):
    # call the hash function above by passing the file and returning the hash
    # table
    words = return_hash(filename)
    # Custom sort on Dict where the second item is returned from each tuple and
    # is sorted in reverse order.
    items = sorted(words.items(), key=func, reverse=False)
    # This is tricky and i forgot. for each entry till 20 count, display key
    # and the value of the dict to display last 20 entries.
    for i in items[:20]:
        print(i[0], i[1])


###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    if len(sys.argv) != 3:
        print ('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    elif option == '--lastcount':
        print_last(filename)
    else:
        print ('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
