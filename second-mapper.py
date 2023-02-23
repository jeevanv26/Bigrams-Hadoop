#!/usr/bin/env python
"""An advanced Mapper, using Python iterators and generators."""

import sys


def read_input(input,separator='\t'):
    for line in input:
        # split the line into words; keep returning each word
        yield line.rstrip().split(separator)


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    for line in data:
        if len(line) < 2:
            continue;
        key = line[0].split('!')
        if len(key) == 2:
            print('%s%s%s' % (key[0], separator, line[0]+' '+line[1]))
        else:
            print('%s%s%s' % (line[0], separator, line[0]+' '+line[1]))
        

# how to test locally in bash/linus: cat <input> | python mapper.py
if __name__ == "__main__":
    main()

