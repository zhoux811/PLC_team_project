from lex import CalcLexer
from time import sleep
import os
import sys


def syntax_error(s):  # for testing
    print(s)
    print('syntax_error')


def lex(s):
    print('\t\t\t\t\t\t\ttoken value: %s \t token type: %s' % (s[0][0], s[0][1]))
    s.pop(0)


def stmt(s):
    print('\tenter <stmt>')
    if s[0][1] == 'VAR_NAME':
        assignment_stmt(s)
    elif s[0][0] == 'Print' or s[0][0] == 'Return':
        func_call(s)
    elif s[0][1] == 'FUNC_NAME':
        variable_declaration(s)
    else:
        print('illegal way to start a statement')
    print('\tleave <stmt>')


def assignment_stmt(s):
    print('\t\tenter <assignment_stmt>')
    lex(s)
    if s[0][0] == '=':
        lex(s)
        if s[0][1] in ['NUM_INT', 'NUM_REAL', 'STRING_LIT', 'FUNC_NAME', 'BOOLEAN_LIT', 'SPECIAL_LIT']:
            expr(s)
        else:
            syntax_error(s)
    else:
        syntax_error(s)
    print('\t\tleave <assignment_stmt>')


def variable_declaration(s):
    print('\t\tenter <variable_declaration>')
    lex(s)
    if s[0][1] == 'VAR_NAME':
        lex(s)
        if s[0][0] == '=':
            lex(s)
            expr(s)
        else:
            print('missing assign = ')
    else:
        syntax_error(s)
    print('\t\tleave <variable_declaration>')


def expr(s):
    print('\t\t\tenter <expr>')
    fac(s)
    sub_expr(s)
    print('\t\t\tleave <expr>')


def sub_expr(s):
    print('\t\t\t\tenter <sub_expr>')
    while True:
        try:
            if s[0][1] == 'ARITH_OP':
                lex(s)
                fac(s)
            else:
                break
        except:
            break
    print('\t\t\t\tleave <sub_expr>')


def fac(s):
    print('\t\t\t\t\tenter <fac>')
    if s[0][1] == 'VAR_NAME':
        lex(s)
    elif s[0][1] == 'FUNC_NAME':
        func_call(s)
    elif s[0][1] in ['NUM_INT', 'NUM_REAL', 'STRING_LIT', 'BOOLEAN_LIT', 'SPECIAL_LIT']:
        lex(s)
    else:
        print('bad/empty fac')
    print('\t\t\t\t\tleave <fac>')


def func_call(s):
    print('\t\t\t\t\t\tenter <func_call>')
    if s[0][1] == 'FUNC_NAME':
        lex(s)
        if s[0][0] == '(':
            lex(s)
            expr(s)
            if s[0][0] == ')':
                lex(s)
                # sleep(10)
            else:
                print('this function call is missing enclosing ) ')
        else:
            print('this function call is missing enclosing ( ')
    else:
        print('illegal function')
        syntax_error(s)
    print('\t\t\t\t\t\tleave <func_call>')


def ini(s):
    if len(s) == 0:
        print('empty line')
        return 0

    type1_value0 = []
    lexer = CalcLexer()
    print('\nline of code: ' + s)
    index = 0
    for tok in lexer.tokenize(s):
        type1_value0.append([tok.value, tok.type])
        index += 1
    # sprint(type0_value1)

    stmt(type1_value0)
    type1_value0.clear()


def main(fname):
    f = open(fname)
    if f:
        print('open file: ' + fname)
    else:
        print('file open error. abort')
        return 0
    for l in f:
        ini(l)
    f.close()


if __name__ == '__main__':
    try:
        main(fname=sys.argv[1])
    except:
        print('you need to specify the input file name')
