# Without reusing the code you wrote for Problem 1, write a new module and a new script.
# Your code need to show the number of pairs of DNA bases in ecoli.fasta in the terminal using
# the function printDigrams provided in the lecture slides.  You might want to practice using
# short.fasta , but your final submission needs to use ecoli.fasta. The second line is

# AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

# which has the pairs AG, GC, CT, TT, TT, TT, TC in order, and so on.

# Create a dictionary that maps strings to the number of times the string appears.
# AA appears 338006 times in the file ecoli.fasta

# If you count the bases in that sample file short.fasta
# and print the result, you would get the following:
# AA appears 18 times, AG appears 9 times, and so on.

# In your terminal, include a short description with each output, e.g.
# "The result is:".  The output should not exceed 100 lines.

def fastaPaircount(filename):
    '''
    Input a file name.
    If the file is a fasta file, output is a printed statement
    showing the number of each letter pair.
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

            # setting up the counts for each letter
            # START CODE HERE

    except FileNotFoundError:
        print("Sorry, I can't find the file", filename)


def printDigrams(pairsCount: Dict[str, int]):
    "Print the digrams"

    bases = ['A', 'G', 'C', 'T']

    # Print the column headings
    print(' ', end=' ')
    for ch in bases:
        print(ch.rjust(7), end=' ')
    print()


    # Print the body of the table
    for ch1 in bases:
        print(ch1, end=' ')

        # Print a row of the table
        for ch2 in bases:
            digram = ch1 + ch2
            if (digram in pairsCount):
                count = pairsCount[digram]
            else:
                count = 0

            # Print count, with formating
            print(repr(count).rjust(7), end=' ')
        print()


def