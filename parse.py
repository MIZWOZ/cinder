import re
import sys
import error as err

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.AST = []
        self.err_code = 255
        #self.advance()
    
    def TT(self, token):
        binop = ['+', '-', '*', '/', '%']
        symbols = ['.', ',', '\\', '@']
        comp_sym = ['&', '|', '=', '==', '!=']
        keyword = ['if', 'fi','else', 'while', 'for', 'in', 'to', 'done']
        definition = ['def', 'int', 'str', 'bool', 'float', 'lst', 'class']
        builtin = ['echo', 'expr']
        
        if token[:1] == '"':
            if token[-1:] != '"':
                err.syntax('End quote not found at: {}'.format(token))
                self.err_code = 1
            else:
                return 'str'
        
        
        if token in keyword:
            return 'keyword'
        elif token in builtin:
            return 'builtin'
        elif token in definition:
            return 'definition'
        if token == '(' or token == ')':
            if token == '(':
                return 'oparen'
            elif token == ')':
                return 'cparen'
        elif token == '{' or token == '}':
            return 'block'
        elif token == '[' or token == ']':
            return 'bracket'
        elif token in binop:
            return 'binop'
        elif token in symbols:
            return 'symbol'
        elif token in comp_sym:
            return 'comparison_symbol'
        
        #for tokens that begin with '-' (negitive numbers)
        if len(token) > 1:  #if token has multiple characters
            if token[:1] == '-': # if tokens first char is '-'
                mod_token = token[1 : : ] # remove '-'
                if mod_token.isdigit(): # check type and return
                    return 'int'
                elif mod_token.replace('.', '',1).isdigit() and mod_token.count('.') < 2:
                    return 'float'
                else: # no number in token and begins with '-' = Error
                    err.syntax('Invalid Syntax at \'-\'')
                    self.err_code = 1
                    return 'error'
        
        if token.isdigit(): # check type and return
            return 'int'
        elif token.replace('.','',1).isdigit() and token.count('.') < 2:
            return 'float'
        else:
            if bool(re.match('^[a-zA-Z]+$', token)): # if it is an assortment of alphabetical
                return 'name'
            else:
                err.token('Unknown token type at: {}'.format(token))
                self.err_code = 3
                return 'error'
        
    def parse(self):
        #tt = 
        
        #keyword
        #definition
        #paren
        #block
        #bracket
        #binop
        #symbol
        #comparison_symbol
        #int
        #float
        #name
        subst = [] # sub syntax tree, appended inside of AST
        line_num = 1
        for i,tok in enumerate(self.tokens):
            
            if tok == '<newline>':
                line_num += 1
                continue
            
            tt = self.TT(tok) # set token type
            
            if tt == 'error': # already printed exception, exit
                sys.exit(self.err_code)
            
            elif tt == 'keyword':
                pass
            
            elif tt == 'builtin':
                if tok == 'echo':
                    if (i+1 < len(self.tokens)): #prevent error
                        next_tt = self.TT(self.tokens[i+1])
                        if next_tt == 'error':
                            sys.exit(self.err_code)
                        if next_tt == 'str':
                            subst = ['echo {}'.format(self.tokens[i+1])]
                            self.AST.append(subst)
                        else:
                            err.order('Expected string type at: {}'.format(self.tokens[i+1]))
                            self.err_code = 6
                            sys.exit(self.err_code)
                    else:
                        for i in self.tokens:
                            i += 1
                            
                        if i < 2: # there is only 1 token, and it is 'echo'
                            err.order('Expected string type at line {} at: {}'.format(line_num, tok))
                            self.err_code = 6
                            sys.exit(self.err_code)
                
                elif tok == 'expr':
                    if (i+1 < len(self.tokens)): #prevent error
                        next_tt = self.TT(self.tokens[i+1])
                        if next_tt == 'error':
                            sys.exit(self.err_code)
                        if next_tt == 'oparen':
                            pass
                        

        return self.AST
     
    def calc(self, tokens): # PEMDAS
        pass
            
    def ast(self): # after tokens have been expanded, they get put in AST
        pass