#!/usr/bin/env python3
import subprocess
import sys
import os

def tree(PATH):
	result = PATH + '\n'
	result += tree_helper(PATH, 0)
	return result 

def tree_helper(PATH, level):
	result = ''
	entries = os.listdir(PATH)
	last = len(entries)
	for i in range(last):
		entry = entries[i]
		if str(entry)[0] == '.' :
			continue
		prefix = ''
		if i == last - 1:
			prefix = get_prefix(1, level)
		else:
			prefix = get_prefix(0, level)
		result += (prefix + entry + '\n')
		if os.path.isdir(entry):
			result += tree_helper(entry, level + 1)
	return result


def get_prefix(is_last, level):
	result = ""
	result += ('    ')*level
	if is_last == 1:
		result += '`-- '
	else:
		result += '|-- '
	return result


if __name__ == '__main__':
	PATH = ''
	if len(sys.argv) < 2:
		# process current directory
		PATH = os.curdir
	else:
		PATH = sys.argv[1]
	print(tree(PATH)) # usage: ./pytree.py [path]
