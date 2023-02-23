#!/usr/bin/env python
"""An advanced Mapper, using Python iterators and generators."""

import sys
import os


def transform_line(line):
    list1 = list(line);
    for i in range(0,len(list1)):
        if (ord(list1[i]) >= 48 and ord(list1[i]) <= 57) or (ord(list1[i]) >= 65 and ord(list1[i]) <= 90) or (ord(list1[i]) >= 97 and ord(list1[i]) <= 122):
            continue;

        else:
            list1[i] = " "

    line = ''.join(list1)
    return line;




def read_input(input):
    for line in input:
        line = transform_line(line);
        # split the line into words; keep returning each word
        if len(line.split()) > 2:
            yield line.split()



def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    word_list = []
    for line in data:
        word_list = []
        for word in line:
           
            word_list.append(word)
            #handles unigrams
            print('%s%s%d' % (word.lower(), separator, 1))
            sys.stderr.write("reporter:counter:HW1,unigram_count,1\n")

        for i in range(0,len(word_list)-1):
            #handles bigrams
            print('%s%s%d' % (word_list[i].lower()+'!'+word_list[i+1].lower(), separator, 1))
            sys.stderr.write("reporter:counter:HW1,bigram_count,1\n")

 

# how to test locally in bash/linus: cat <input> | python mapper.py
if __name__ == "__main__":
    main()


