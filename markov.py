"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    filename = open(file_path)  #just opening a filepath (but using with will close it automatically)
    text = filename.read() #reads the whole file instead (opposite of .readlines())
    filename.close() #closes the file

    return text

print(open_and_read_file('green-eggs.txt'))


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """


    chains = {}

    words = text_string.split()
    # print(words)

    for index in range(len(words) -2):  #same as range(0, len(words))
        key = (words[index], words[index + 1])
        value = words[index + 2]
        if key not in chains:
            chains[key] = []
        chains[key].append(value)  #append works bc we're accessing the value which is a list


    print(chains)

    return chains


def make_text(chains):
    """Return text from chains."""
    words = [] 

    current_key = choice(list(chains.keys())) 
    
    while current_key in chains:  
        chosen_word = choice(chains[current_key])
        words.append(chosen_word)

        new_key = (current_key[-1], chosen_word) 

        current_key = new_key

        # print('CURRENT KEY:', current_key) 
        # print('CHOSEN WORD:', chosen_word)
        # print('NEW KEY:', str(new_key))

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
