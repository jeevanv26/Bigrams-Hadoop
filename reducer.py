#!/usr/bin/env python
"""An advanced Reducer, using Python iterators and generators."""

import sys


# receive the output of a mapper, (key, [value, value, ...])
def read_mapper_output(input, separator='\t'):
    for line in input:
        #  return each (key, [value, value, ...]) tuple, though there should only be one per line
        yield line.rstrip().split(separator, 1)


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    current_key = '$'
    total_count = 0

    #my own reducer; assumption is that the keys come in sorted
    for line in data:
        try:
            if current_key == '$':
                if len(line) >=2:
                    total_count += int(line[1])
                    current_key = line[0] 

            elif line[0] == current_key:
                if len(line) >=2:
                    total_count += int(line[1])
            else:
                print('%s%s%d' % (current_key, separator, total_count))
                if len(line) >=2:
                    current_key = line[0] 
                    total_count = int(line[1])
                else:
                     current_key = '$'
                     total_count = 0


        except ValueError:
            pass
    if current_key != '$':
        print('%s%s%d' % (current_key, separator, total_count))


if __name__ == "__main__":
    main()
