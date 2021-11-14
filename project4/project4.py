"""
Math 560
Project 4
Fall 2021

Partner 1: Kaifeng Yu(ky99)
Partner 2: Fangting Ma(fm128)
Date:
"""

# Import p4tests.
from p4tests import *

################################################################################

"""
ED: the edit distance function
"""
def ED(src, dest, prob='ED'):
    # Check the problem to ensure it is a valid choice.
    if (prob != 'ED') and (prob != 'ASM'):
        raise Exception('Invalid problem choice!')
    
    # initialization: set all entries in dp table to [0, ' ']
    dp_table=[[[0,' '] for _ in range(len(dest)+1)] for _ in range(len(src)+1)]
    # set first row, if prob = 'ASM', do not set
    if prob == 'ED' :
        for i in range(1, len(dest) + 1):
            dp_table[0][i] = [i, 'L']
    # set first column
    for i in range(1, len(src) + 1):
        dp_table[i][0] = [i, 'U']
    # fill the dp table
    for i in range(1, len(src) + 1):
        for j in range(1, len(dest) + 1):
            if src[i - 1] == dest[j - 1]:
                dp_table[i][j][0] = dp_table[i - 1][j - 1][0]
                dp_table[i][j][1] = 'D'
            else:
                if dp_table[i-1][j-1][0] < dp_table[i][j-1][0] and \
                        dp_table[i-1][j-1][0] < dp_table[i-1][j][0]:
                    dp_table[i][j][0] = dp_table[i-1][j-1][0] + 1
                    dp_table[i][j][1] = 'D'
                elif dp_table[i][j-1][0] < dp_table[i-1][j][0]:
                    dp_table[i][j][0] = dp_table[i][j-1][0] + 1
                    dp_table[i][j][1] = 'L'
                else:
                    dp_table[i][j][0] = dp_table[i-1][j][0] + 1
                    dp_table[i][j][1] = 'U'
    
    #for i in range(len(src) + 1):
    #    print(dp_table[i])
    dist = dp_table[len(src)][len(dest)][0]
    # reconstruct an optimal set of edits
    edits = []
    m = len(src)
    n = len(dest)
    while dp_table[m][n][1] != ' ':
        if dp_table[m][n][1] == 'U':
            edit = ('delete', src[m-1], m-1)
            m = m-1
        elif dp_table[m][n][1] == 'L':
            edit = ('insert', dest[n-1], m)
            n = n-1
        else: 
            if dp_table[m][n][0] == dp_table[m-1][n-1][0]:
                edit = ('match', src[m-1], m-1)
            else:
                edit = ('sub', dest[n-1], m-1)
            m = m-1
            n = n-1
        edits.append(edit)
    return dist, edits

################################################################################

"""
Main function.
"""
if __name__ == "__main__":
    edTests(False)
    print()
    compareGenomes(True, 30, 300, 'ED')
    print()
    compareRandStrings(True, 30, 300, 'ED')
    print()
    compareGenomes(True, 30, 300, 'ASM')
    print()
    compareRandStrings(True, 30, 300, 'ASM')
