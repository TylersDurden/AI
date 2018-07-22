import math
import sys

class driver:

    PuzzleInit = []
    modes = ['-dfs','-bfs','-a*']
    Mode = ''

    def __init__(self, mode,initial_puzzlestate):
        self.Mode = mode
        self.PuzzleInit = initial_puzzlestate
        print(int(math.sqrt(len(initial_puzzlestate))))


def usage():
    print('********************************************')
    print('* Incorrect Usage! Correct examples:       *')
    print('* python driver.py -dfs [1,5,4,3,0,6,7,2,8]*')
    print('********************************************')



def main():
    if len(sys.argv) < 3:
        usage()
    else:
        print('mode: '+sys.argv[1])
        print('Initial State: '+sys.argv[2])


if __name__=='__main__':
    main()