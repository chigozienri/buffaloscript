#!/usr/bin/env python3
import nltk
import sys

from nltk import CFG

def parse(string):
    # Note that this grammar does not accept "Buffalo buffalo" as a
    # verb phrase (meaning "to buffalo in a way unique to Buffalo"),
    # as illustrated here: https://cse.buffalo.edu/~rapaport/buffalobuffalo.html
    # Accepting this would make the final buffaloscript much easier to
    # write in a way that guarantees any program is grammatical, but
    # feels awkward in real English (Pinker agrees)
    grammar_string = """
    S -> V | VP
    NP -> NP NP V | A N | N
    VP -> NP V NP | NP V
    V -> 'buffalo'
    N -> 'buffalo'
    A -> 'Buffalo'
    """

    grammar = CFG.fromstring(grammar_string)

    parser = nltk.ChartParser(grammar)
    
    return list(parser.parse(string.split()))

def parses(string):
    if len(parse(string)) > 0:
        return True
    return False

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1][-4:] != '.buf':
            filepath = str(sys.argv[1]) + '.buf'
        else:
            filepath = str(sys.argv[1])

        with open(filepath, 'r') as f:
            string = f.read()

    elif len(sys.argv) == 1:
        string = sys.stdin.read()
    else:
        print(f'usage: {sys.argv[0]} <src>\nor cat <src.buf> | {sys.argv[0]}')
        sys.exit(1)

    sys.stdout.write(str(parse(string)))