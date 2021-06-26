"""
File: anagram_faster.py
Name: Sharlene Chen
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
word_list = {}

def main():
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        word = input('Find anagrams for: ')
        if word != '-1':
            print('Searching...')
            read_dictionary()
            find_anagrams(word)
        else:
            break

def read_dictionary():
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip()
            word_list[word] = ''    #saving all words in a dictionary to speed up


def find_anagrams(s):
    """
    :param s: the word to be rearranged
    :return: the printed anagram list
    """
    alphabets = {}
    anagram = []
    length = len(s)
    for i in range(len(s)): #saving all letters as index numbers
        alphabets[i] = s[i]
    lst = helper('',[],length)  #returns a list of index that contains all combinations at len(s)
    for i in range(len(lst)):
        word = ''
        for letters in lst[i]:  #looping through all index combinations in lst and transforming back to words
            word += alphabets[int(letters)]
        if word not in anagram and word in word_list:
            print(f'Found: {word}')
            print('Searching...')
            anagram.append(word)
    print(f'{len(anagram)} anagrams: {anagram}')


def helper(maybe_i,result,length):
    if len(maybe_i) == length:
        result.append(maybe_i)
        return result
    else:
        for i in range(length):
            index = str(i)
            if index in maybe_i:
                pass
            else:
                #choose
                maybe_i += index    #getting all possible combinations of indexes at len(s)
                #explore
                helper(maybe_i,result,length)
                #unchoose
                maybe_i = maybe_i[0:len(maybe_i)-1]
        return result

def has_prefix(sub_s):
    """
    :param sub_s:
    :return: True / False if a word that starts with sub_s exists
    """
    pass


if __name__ == '__main__':
    main()
