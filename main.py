from lexer import Lexer
from parse import Parser

master_tokens = []

def inf():

    while True:
        text = input('test > ')

        lexer = Lexer(text)
        tokens = lexer.lex()

        print('TOKENS:')
        print(tokens) # print tokens
        
        parser = Parser(tokens)
        ast = parser.parse()
        
        print("AST:")
        print(ast)
        
def fin():
    text = 'the buig' + '\n' + 'boi'
    lexer = Lexer(text)
    tokens = lexer.lex()
    
    print(tokens)
 
def testfile():
    with open("test.cdr", "r") as a_file:
        
        print('TOKENS:')
        for line in a_file:
            text = line.strip()
            lexer = Lexer(text)
            tokens = lexer.lex()
            for tok in tokens:
                master_tokens.append(tok)
            master_tokens.append('<newline>')
                
    print(master_tokens)
            
    parser = Parser(master_tokens)
    ast = parser.parse()  
    
    print('\n' + "AST:")
    print(ast)
    
    #interpreter
    
    print('\n' + "OUTPUT:")
    
    
#inf()
#fin()
testfile()