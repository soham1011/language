TT_INT = 'TT_INT'
TT_FLOAT = 'TT_FLOAT'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_LPAREN = 'LEFTPAREN'
TT_RPAREN = 'RPARENT' 
DIGITS = '1234567890'

class Token:
    def __init__(self,type_,value):
        self.type = type_
        self.value = value
    def __repr__(self):
        if self.value:
            return f'{self.type}:{self.value}'
        return f'{self.type}'
class Error:
    def __init__(self,error_name,details):
        self.error_name = error_name
        self.details = details
        
    
class Lexer:
    def __init__(self,text):
        self.text = text
        self.pos = -1 
        self.current_char = None
        self.advance
    def advance(self):
        self.pos = self.pos + 1 
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
    def make_tokens(self):
        tokens = []
        while self.current_char != None:
            if self.currentchar in '\t':
                self.advance()
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS))
                self.advance()    
            elif self.current_char == '*':
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN))
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
                self.advance()
        return tokens
    def make_number(self):
         num_str = ''
         dot_count = 0 
         while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                 if dot_count == 1 :
                     break
                 dot_count = dot_count + 1 
                 num_str = num_str + '.'
            else:
             num_str = num_str + self.current_char
            if dot_count == 0:
                return Token(TT_INT,int(num_str))
            else:
                return Token(TT_FLOAT,float(num_str))
