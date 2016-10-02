#!/usr/bin/env python3
import subprocess
import sys
import os

BLANK = '    '
STEM = '│   '
LEAF = '├── '
LEAF_LAST = '└── '

# python implementaion of bash "tree" command
def tree(path):
    result = path + '\n'
    [result_r, dir_ct_r, file_ct_r] = \
        tree_helper(path, 0, 0, '')
    result += result_r
    return [result, dir_ct_r, file_ct_r]


# helper method for recursive calls
def tree_helper(path, dir_ct, file_ct, prefix):
    result = ''
    entries = os.listdir(path)

    # find last directory
    last_dir = ''
    for entry in entries:
    	if os.path.isdir(path + '/' + entry):
    		last_dir = entry

    for i in range(len(entries)):
        # root_last_r = 0  ## root_last value for recursive call
        # ignore hidden files
        entry = entries[i]
        if str(entry)[0] == '.':
            continue

        # determine leaf representaion
        prefix_r = prefix
        if i == len(entries) - 1:
            # root_last_r = 1
            result += (prefix + LEAF_LAST + entry + '\n')
            prefix_r += BLANK
            # prefix = get_prefix(root_last, 1, level)
        else:
            # prefix = get_prefix(root_last, 0, level)
            result += (prefix + LEAF + entry + '\n')
            prefix_r += STEM

        # # update prefix
        # prefix_r = prefix
        # if entry == last_dir:
        # 	prefix_r += BLANK
        # else:
        # 	prefix_r += STEM

        entry_with_path = path + '/' + entry
        # if path not specified, entry might not be found
        if os.path.isdir(entry_with_path):
            dir_ct += 1
            [result_r, dir_ct_r, file_ct_r] = \
                tree_helper(entry_with_path, dir_ct, file_ct, prefix_r)
            result += result_r
            dir_ct = dir_ct_r
            file_ct = file_ct_r
        else:
            file_ct += 1
    return [result, dir_ct, file_ct]


if __name__ == '__main__':
    path = ''
    if len(sys.argv) < 2:
        # process current directory
        path = os.curdir
    else:
        path = sys.argv[1]
    [result, dir_ct, file_ct] = tree(path)
    print(result)
    dir_string = ''
    file_string = ''
    if dir_ct > 1:
        dir_string = "directories"
    else:
        dir_string = "directory"
    if file_ct > 1:
        file_string = "files"
    else:
        file_string = "file"
    print(str(dir_ct) + " " + dir_string + ", " \
        + str(file_ct) + " " + file_string)
