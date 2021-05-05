from sly import Lexer
import os
import sys


class CalcLexer(Lexer):
    # Set of token names.   This is always required
    tokens = {
        VAR_NAME, FUNC_NAME,
        NUM_INT, NUM_REAL, STRING_LIT, BOOLEAN_LIT, SPECIAL_LIT,
        ARITH_OP,
        ASSIGN, PAREN_L, PAREN_R,

    }

    # String containing ignored characters between tokens
    ignore = ' \t\n'

    # Regular expression rules for tokens
    VAR_NAME = r'[a-z][a-zA-Z0-9]{0,9}'
    FUNC_NAME = r'[A-Z][a-zA-Z0-9]{0,9}'

    NUM_INT = r'-?[\d]{1,5}'
    NUM_REAL = r'-?[\d]{1,9}\.[\d]{1,9}'
    STRING_LIT = r'".{1,99}"'
    BOOLEAN_LIT = r'_True|_False'
    SPECIAL_LIT = r'_None|_Null'

    ARITH_OP = r'\+|-|\*|/|%'

    ASSIGN = r'='
    PAREN_L = r'\('
    PAREN_R = r'\)'

    literals = {'(', ')', '{', '}', ';'}


def main(fname):
    line_n = 0
    f = open(fname, 'r')
    if f:
        print('open file: ' + fname)
    else:
        print('file open error. abort')
        return 0
    for line in f:
        lexer = CalcLexer()
        print('\n\n\nline_n: ' + str(line_n) + ' : ' + line)
        for tok in lexer.tokenize(line):
            print('\ttype=%r,  \tvalue=%r' % (tok.type, tok.value))
        line_n += 1
    f.close()


if __name__ == '__main__':
    try:
        main(fname = sys.argv[1])
    except:
        print('you need to specify the input file name')
