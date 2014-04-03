""" 
Algorithm to remove duplicates from a string, but keep the first
"""
import time

string = 'The quick brown fox jumps over the lazy dog'
#Using Python's internal method
string_set = set(string)
#Returns unique characters, but not in the original order
print string_set


def remove_duplicates(string_in):
	char_array = [0]*256
	string_out = []
	for char in string_in:
		if char_array[ord(char)] == 0:
			char_array[ord(char)] =+1
			string_out.append(char)
	return string_out

print remove_duplicates(string)

