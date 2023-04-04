#!/usr/bin/python3

import sys
from random import randint

# Environment variables
filename = 'dicewarewordlist.txt'


def make_dict(filename):
    """
    Reads in the word list, and creates a dictionary with the random number as the key,
    and the word as the returned value.

    Inputs: Filename for wordlist

    Outputs: Dictionary of wordlist

    Author: Gabe Miles
    """
    f = open('dicewarewordlist.txt', 'r')
    word_dict = {}
    counter = 0
    key = -1
    value = ''

    for line in f:
        for word in line.split():
            if counter % 2 == 0:
                key = word
            else:
                value = word
                word_dict[key] = value
            counter += 1
    
    return word_dict

def print_words(words, num_words):
    print("Thanks for using Passphrase! Use the folowing {} words in your passphrase:\n".format(num_words))
    line = ''
    for i in range(1,num_words + 1):
        line = line + 'Word #{:<10}'.format(str(i))
    print(line)

    line = ''
    for word in words:
        line = line + '{:<16}'.format(word)
    print(line)

    print("\nBe sure to add other alphanumeric characters and capitalization to your new passphrase. Safe travels!")


def gen_words():
    """
    Generates random keys for words dictionary, and returns a specified number of values.

    Input: Command line argument with number of values to return

    Output: Command line formatted output with number of values requested

    Author: Gabe Miles 
    """
    # Default value
    num_words = 3
    
    words = []
    word_dict = make_dict(filename)

    if (args_count := len(sys.argv)) > 2:
        print("One argument expected, got {}".format(args_count - 1))
        raise SystemExit(2)

    if args_count == 2:
        num_words = int(sys.argv[1])

    for i in range(num_words):
        key = ''
        for j in range(5):
            digit = randint(1,6)
            key = key + str(digit)

        word = word_dict[key]
        words.append(word)

    return words, num_words

# Run program for command-line
words, num_words = gen_words()
print_words(words, num_words)