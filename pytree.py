#!/usr/bin/env python3
import subprocess
import sys
import os


# python implementaion of bash "tree" command
def tree(PATH):
    result = PATH + '\n'
    [result_r, dir_ct_r, file_ct_r] = \
        tree_helper(PATH, 0, 0, 0)
    result += result_r
    return [result, dir_ct_r, file_ct_r]


# helper method for recursive calls
def tree_helper(PATH, level, dir_ct, file_ct):
    result = ''
    entries = os.listdir(PATH)
    last = len(entries)
    for i in range(last):
        entry = PATH + '/' + entries[i]
        # ignore hidden files
        if str(entry)[0] == '.' :
            continue
        prefix = ''
        if i == last - 1:
            prefix = get_prefix(1, level)
        else:
            prefix = get_prefix(0, level)
        result += (prefix + entry + '\n')
        if os.path.isdir(entry):
            dir_ct += 1
            [result_r, dir_ct_r, file_ct_r] = \
                tree_helper(entry, level + 1, dir_ct, file_ct)
            result += result_r
            dir_ct = dir_ct_r
            file_ct = file_ct_r
        elif os.path.isfile(entry):
            file_ct += 1
    return [result, dir_ct, file_ct]


# return the visual prefix for tree printing
def get_prefix(is_last, level):
    result = ""
    result += ('    ') * level
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
    [result, dir_ct, file_ct] = tree(PATH)
    print(result)
    print(str(dir_ct) + " directory, " + str(file_ct) + " files")
