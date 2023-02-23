#!/usr/bin/env python
"""An advanced Reducer, using Python iterators and generators."""

import sys


def extract_info(pair):
    k_v = pair.split()
    return k_v[0],int(k_v[1])


# receive the output of a mapper, (key, [value, value, ...])
def read_mapper_output(input, separator='\t'):
    for line in input:
        #  return each (key, [value, value, ...]) tuple, though there should only be one per line
        yield line.rstrip().split(separator)


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    current_key = '$'
    key_value = 0
    string = ''
    value = 0

    for line in data:
        if current_key == '$':
            if len(line) >=2:
                current_key = line[0]
                string, key_value = extract_info(line[1])
                
        elif line[0] == current_key:
            string, value = extract_info(line[1])
            probability = (float(value)/9573750)/(float(key_value)/9578487)
            output_string = string.split('!')[1]+'|'+ current_key
            print('%s%s%f' % (output_string, separator,probability))

        else:
            if len(line) >=2:
                current_key = line[0] 
                string, key_value = extract_info(line[1])
            else:
                current_key = '$'
                key_value = 0
                string = ''
                value = 0
    



if __name__ == "__main__":
    main()