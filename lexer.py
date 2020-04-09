import error as err

class Lexer:
    def __init__(self, text):
        self.text = text
        
    def process_toks(self, tokens):
        for i,char in enumerate(tokens):
            if char == '':
                tokens.pop(i)
        return tokens
        
    def lex(self):
        string = self.text
        tokens = []
        white_space = ' '
        cmt = False
        tid = ''
        
        symbols = ['(', ')', '{', '}', '[', ']', '.', '*', '\n', ':', ','] #single char keywords
        #other_symbols = ['\\', '/*', '*/'] # multi-char keywords
        keywords = ['class', 'def', 'int', 'str', 'bool', 'print']
        KEYWORDS = symbols + keywords #+ other_symbols
        binop = ['+', '-', '*', '/', '%']
        seperators = ['(', ')', '{', '}', '[', ']']
        
        
        lexeme = ''
        for i,char in enumerate(string):
            if char == "#" and cmt == False: #comments
                cmt = True
                continue
            elif cmt == True: #comments
                continue
            elif char == '\n' and cmt == True: #comments
                cmt == False
                continue
            
            if char == '"' and tid != 'str': #quotes/strings
                tid = 'str'
                continue
            elif tid == 'str' and char != '"': #quotes/strings
                lexeme += char
                continue
            elif tid == 'str' and char == '"': #quotes/strings
                tid = ''
                tokens.append("\"" + lexeme + "\"")
                lexeme = ''
                continue
            
            if char in seperators: # ( ) [ ] { }
                tokens.append(lexeme)
                tokens.append(char)
                lexeme = ''
                continue

            if char != white_space:
                lexeme += char # adding a char each time
            if (i+1 < len(string)): # prevents error             
                if string[i+1] == white_space: #or string[i+1] in KEYWORDS or lexeme in KEYWORDS: # if next char == ' '
                    if lexeme != '':
                        #print(lexeme.replace('\n', '<newline>'))
                        tokens.append(lexeme.replace('\n', '<newline>'))
                        lexeme = ''
                
        tokens.append(lexeme)
        
        tokens = self.process_toks(tokens) # gets rid of blank indexes - ex: ''
        return tokens