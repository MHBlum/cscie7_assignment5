"""a module that takes an input file, determines if the file is a
fasta file, and then counts the number of A,C,G, and T in the sequence.
If the file is not a fasta file, an exception will be thrown."""

# param filename: a string which is the name of the file,
# for example 'ecoli.fasta'
# returns: an exception if the file does not end in .fasta
# returns: a table of values for each letter in the fasta file.


def fastaCount(filename):
    '''
    Input a file name.
    If the file is a fasta file, output is a printed statement
    showing the number of each letter
    If not a fasta file, output is an exception statement.
    '''
    try:
        # checks if the last 6 characters are .fasta
        if filename[-6:] != '.fasta':
            print("The file you have entered is not a .fasta file.")
        else:
            # reading in the file
            filetmp = open(filename, 'r')

            # skip the first info line; we care about the following content
            contentHead = filetmp.readline()

            # read in the remainder of teh file as a temporary content variable
            content = filetmp.read()

            # setting up the counts
            countA = 0
            countC = 0
            countG = 0
            countT = 0

            for char in content:
                if char == 'A':
                    countA = countA + 1
                elif char == 'C':
                    countC = countC + 1
                elif char == 'G':
                    countG = countG + 1
                elif char == 'T':
                    countT = countT + 1

            print('A ', countA)
            print('C ', countC)
            print('G ', countG)
            print('T ', countT)

    except FileNotFoundError:
        print("Sorry, I can't find the file", filename)
