
#Exit Code Values
    
#in order -
  
#unkown error is err code 255
    
#1
def syntax(msg):
    print('SyntaxError: {}'.format(msg))
    
#2
def value(msg):
    print('ValueError: {}'.format(msg))
    
#3
def token(msg):
    print('TokenError: {}'.format(msg))
    
#4    
def glob(msg):
    print('GlobError: {}'.format(msg))
    
#5    
def parse(msg):
    print('ParseError: {}'.format(msg))
    
#6    
def order(msg):
    print('OrderError: {}'.format(msg))