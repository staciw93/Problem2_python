import re
import sys
import os

for directory, subdirectories, files in os.walk(sys.argv[1]):
    for file in files:
        inputfile = open(os.path.join(directory, file), "r")
        outputfile = open(os.path.join(sys.argv[2], "redacted" + file), "w")
        ssn = re.compile(r'[0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]')
        for line in inputfile:
            for word in line.split():
                if ssn.search(word):
                    word = re.sub('\d', '*', word)
                outputfile.write(word + " ")

        inputfile.close()
        outputfile.close()
