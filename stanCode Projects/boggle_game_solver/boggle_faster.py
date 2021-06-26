"""
File: boggle_faster.py
Name: Sharlene Chen
----------------------------------------
TODO: Boggle is an application that finds out all possible words with more than 4 letters from a 4x4 grid.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
word_dict = {}

def main():
	"""
	TODO: Prompts the user to input the desired letters to be used in the game boggle.
	"""
	letter_dict = {}
	first_row = input('1 row of letters: ')
	first_row = first_row.split(' ')
	for i in range(len(first_row)):
		if first_row[i].isalpha() is False or len(first_row[i]) != 1:
			print('Illegal Input')
			exit()
		else:
			first_row[i] = first_row[i].lower()
			letter_dict[(0,i)] = first_row[i]
	second_row = input('2 row of letters: ')
	second_row = second_row.split(' ')
	for i in range(len(second_row)):
		if second_row[i].isalpha() is False or len(second_row[i]) != 1:
			print('Illegal Input')
			exit()
		else:
			second_row[i] = second_row[i].lower()
			letter_dict[(1, i)] = second_row[i]
	third_row = input('3 row of letters: ')
	third_row = third_row.split(' ')
	for i in range(len(third_row)):
		if third_row[i].isalpha() is False or len(third_row[i]) != 1:
			print('Illegal Input')
			exit()
		else:
			third_row[i] = third_row[i].lower()
			letter_dict[(2, i)] = third_row[i]
	fourth_row = input('4 row of letters: ')
	fourth_row = fourth_row.split(' ')
	for i in range(len(fourth_row)):
		if fourth_row[i].isalpha() is False or len(fourth_row[i]) != 1:
			print('Illegal Input')
			exit()
		else:
			fourth_row[i] = fourth_row[i].lower()
			letter_dict[(3, i)] = fourth_row[i]
	length = int(abs(len(letter_dict) ** (1 / 2)))
	read_dictionary(letter_dict,length)
	boggle(letter_dict,length)

def boggle(letter_dict,length):
	lst = {}
	for i in range(length):	# looping through first letters
		for j in range(length):
			helper(letter_dict,lst,{},'',i,j,length)
	print(f'There are {len(lst)} words in total.')

def helper(letter_dict,result,maybe_i,maybe_word,y,x,length):
	if has_prefix(maybe_word) is False:	# skip if no words start with this maybe_word combination
		pass
	else:
		if x == 0 and y == 0:  # for the four corners
			minx, maxx, miny, maxy = x, x + 1, y, y + 1
			# setting the coordinates of their neighbors that will be looped later
		elif x == length - 1 and y == 0:
			minx, maxx, miny, maxy = x - 1, x, y, y + 1
		elif x == 0 and y == length - 1:
			minx, maxx, miny, maxy = x, x + 1, y - 1, y
		elif x == length - 1 and y == length - 1:
			minx, maxx, miny, maxy = x - 1, x, y - 1, y
		elif x == 0 and (y != 0 and y != length - 1):  # for the four sides
			minx, maxx, miny, maxy = x, x + 1, y - 1, y + 1
		elif (x != 0 and x != length - 1) and y == 0:
			minx, maxx, miny, maxy = x - 1, x + 1, y, y + 1
		elif x == length - 1 and y != 0 and y != length - 1:
			minx, maxx, miny, maxy = x - 1, x, y - 1, y + 1
		elif x != 0 and x != length - 1 and y == length - 1:
			minx, maxx, miny, maxy = x - 1, x + 1, y - 1, y
		else:  # letters in the middle
			minx, maxx, miny, maxy = x - 1, x + 1, y - 1, y + 1
		for i in range(miny, maxy + 1):  # looping through all the neighboring letters
			for j in range(minx, maxx + 1):
				index = (i,j)	# ensure no repeated letters are going into the string
				if index in maybe_i:
					pass
				else:
					#choose
					maybe_i[index] = ''
					maybe_word += letter_dict[index]
					if len(maybe_word) < length:	# keep looping if maybe_word isn't long enough
						helper(letter_dict, result, maybe_i, maybe_word, i, j, length)
					else:
						if maybe_word not in result:	# check if in result already
							if maybe_word in word_dict:	# check if in dictionary
								print(f'Found: {maybe_word}')
								result[maybe_word] = ''
					#explore
						helper(letter_dict,result,maybe_i,maybe_word,i,j,length)
					#unchoose
					maybe_word = maybe_word[0:len(maybe_word) - 1]
					maybe_i.pop((i,j))
	return result

def read_dictionary(letter_dict,length):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	letter_lst = {}
	for i in range(length):
		for j in range(length):
			if letter_dict[(i,j)] in letter_lst:
				pass
			else:
				letter_lst[letter_dict[(i,j)]] = ''	# list of letters that could be in the words
	with open(FILE, 'r') as f:
		for line in f:
			word = line.strip()
			if len(word) >= length:
				count = 0	# count of all letters
				for i in range(len(word)):
					if word[i] not in letter_lst:	# if encounter letter is not on the grid, can eliminate
						break
					else:
						count += 1
				if count == len(word):	# if all letter in a particular word is in dictionary, can be read into the dict
					word_dict[word] = ''
	print(word_dict)

def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for words, placeholder in word_dict.items():
		if words.startswith(sub_s) is True:
			return True
	return False



if __name__ == '__main__':
	main()
