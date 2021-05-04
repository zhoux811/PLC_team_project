from sly import Lexer


class CalcLexer(Lexer):
    # Set of token names.   This is always required
    tokens = {
        VAR_NAME, FUNC_NAME,
        NUM_INT, NUM_REAL,
        OP_PLUS, OP_MINUS, OP_TIMES, OP_DIVIDE, OP_MODULO,
        ASSIGN, PAREN_L, PAREN_R

    }

    # String containing ignored characters between tokens
    ignore = ' \t'

    # Regular expression rules for tokens
    VAR_NAME = r'[a-z][a-zA-Z0-9]{0,9}'
    FUNC_NAME = r'[A-Z][a-zA-Z0-9]{0,9}'

    NUM_INT = r'[\d]{1,5}'
    NUM_REAL = r'[\d]{1,9}\.[\d]{1,9}'

    OP_PLUS = r'\+'
    OP_MINUS = r'-'
    OP_TIMES = r'\*'
    OP_DIVIDE = r'/'
    OP_MODULO = r'%'

    ASSIGN = r'='
    PAREN_L = r'\('
    PAREN_R = r'\)'


if __name__ == '__main__':
    samples = '''x = 3 + 42 * s - t
a = Function(a+b)
b = Function1(a+b) * Function2( Function3(4 % n) )'''
    line_n = 0
    for line in samples.split(sep='\n'):
        lexer = CalcLexer()
        print('\n\n\nline_n: ' + str(line_n) + ' : ' + line)
        for tok in lexer.tokenize(line):
            print('\ttype=%r,  \tvalue=%r' % (tok.type, tok.value))
        line_n += 1