# -*- coding: utf-8 -*-

import codecs
import sys

# given a mapping file with comma separated values,
# encode the other filenames passed in

mapping = dict()

def main(mappingFile, totranslate):

    # is a comma separated file giving the mappings
    for line in codecs.open(mappingFile, encoding='utf-8', mode='r'):
        elements = line.split(',')
        mapping[elements[1].strip()] = elements[0].strip()

    for fn in totranslate:
        with codecs.open(fn + '.token', mode='w') as output:
            for line in codecs.open(fn, encoding='utf-8', mode='r'):
                elements = line.strip().split(' ')
                all_in = True
                pool = []
                for element in elements:
                    if element not in mapping:
                        all_in = False
                        break
                    else:
                        pool.append(mapping[element])
                if all_in:
                    for unit in pool[:-1]:
                        output.write(unit)
                        output.write(' ')
                    output.write(pool[-1])
                    output.write('\n')

if __name__ == "__main__":

    # need at least the mapping file and one other, 
    # plus the program name in 0
    if len(sys.argv) < 3:
        print "usage: python", sys.argv[0], "mapfilename filetoencode1 [filetoencode2 ...]"
        print "       tokens are split on whitespace only"
        print "       translated files are given a .token suffix"
    else:
        # sys.argv[0] is the filename of the program
        mappingFile = sys.argv[1]
        totranslate = sys.argv[2: ]
        main(mappingFile, totranslate)