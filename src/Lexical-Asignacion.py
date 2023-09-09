# Using ply - lexer we are going to:
# create our custom tokens with our regular expressions.
# This later will be sent to the ply-lexer and build the 
# machine that will interpret our code. For this instance
# the machine will ONLY scan the code and tokenize all
# elements inside the test program provided as a text file

# import ply lexer
import ply.lex as lex

# List of keywords
keywords = {
    'print': 'PRINT',
    'while': 'WHILE',
    'if': 'IF',
    'else': 'ELSE',
    'int': 'INT_TYPE',
    'double': 'DOUBLE_TYPE',
}

# Declaration of the assigned tokens
# for lexer from ply to use when scanning the code
tokens = [
    'ID',          # consists of: [a-z|A-Z]+[0-9]+
    'INT',         # consists of: [1-9]+[0-9]+
    'DOUBLE',      # consists of: double-precision representation
    'COMMENT',     # consists of: [//][ascii | \n]
    'WHITESPACE',  # consists of: [ascii9 | \t] | [ascii10 | \n] | [ascii13 | \r] | [ascii32 | spcace]
    
    # Delimeters represented in string
    'RO',          # (
    'RC',          # )
    'BO',          # {
    'BC',          # }
    'SO',          # [
    'SC',          # ]

    # Operators represented in string
    'EQ',       # =
    'NOT',      # ! 
    'OR',       # |
    'AND',      # &
    'MIN',      # <
    'MAJ',      # >
    'MIN_EQ',   # <=
    'MAJ_EQ',   # >=
    'PLUS',     # +
    'MINUS',    # -
    'STAR',     # *
    'DIV',      # /
    'CM',       # ,
    'S'         # ;
] + list(keywords.values())

# Single-character tokens
t_RO = r'\('
t_RC = r'\)'
t_BO = r'\{'
t_BC = r'\}'
t_SO = r'\['
t_SC = r'\]'
t_EQ = r'='
t_NOT = r'!'
t_OR = r'\|'
t_AND = r'&'
t_MIN = r'<'
t_MAJ = r'>'
t_MIN_EQ = r'<='
t_MAJ_EQ = r'>='
t_PLUS = r'\+'
t_MINUS = r'-'
t_STAR = r'\*'
t_DIV = r'/'
t_CM = r','
t_S = r';'

# Regular expression rules
t_ignore = ' \t\r'  # Ignore space, tab, and carriage return

def t_COMMENT(t):
    r'//[^\\n]*'
    pass  # Ignore comments

def t_WHITESPACE(t):
    r'\n'
    pass  # Newlines are ignored

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = keywords.get(t.value, 'ID')  # Check if it's a keyword
    return t

def t_DOUBLE(t):
    r'-?\d+\.\d+([Ee][+-]?\d+)?'
    return t

def t_INT(t):
    r'-?[1-9]\d*|0'
    return t

# Build the lexer
lexer = lex.lex()

# Create the scanner machine (lexer) to tokenize
# the given input program file (Test_program.txt)
# source_file = open('Test_program.txt', 'r')

# Obtain the source code from source file

# source_code = source_file.read()

source_code = '''
int variable = 10;
'''

# Feed the lexer with the source code
lexer.input(source_code)

while True: 
    token = lexer.token()

    if not token:
        break
    
    print(token)