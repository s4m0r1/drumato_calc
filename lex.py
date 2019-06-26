import sys
from token import Token,TokenType
OPERATOR = {'+': TokenType.PLUS,
            '-': TokenType.MINUS,
            '*': TokenType.MULTIPLE,
            '/': TokenType.DIVISION}

class Lexer:
    def __init__(self, inpiut_str: str):
        self.input = inpiut_str
        self.pos = 0
    
    def read_number(self) -> str:
        start = self.pos
        while self.is_number(self.input[self.pos]):
            self.pos += 1
        return self.input[start:self.pos]
    
    def is_number(self, char: 'one character') -> bool:
        return 0x30 <= ord(char) and ord(char) <= 0x39

    def next_token(self) -> Token:
        self.skip_whitespace()
        if self.pos >= len(self.input):
            return Token(TokenType.EOF, "\x00")
        elif self.is_number(self.input[self.pos]):
            number = self.read_number()
            if self.input[self.pos] in [' ', '\t', '\n']:
                self.pos += 1
            return Token(TokenType.NUMBER, number)
        elif self.input[self.pos] in '+-*/':
            op = self.input[self.pos]
            self.pos += 1
            return Token(OPERATOR[op], op)
        elif self.input[self.pos] == '\x00':
            return Token(TokenType.EOF, "\x00")
        else:
            print(
                f"invalid token:{self.input[self.pos].string()}")
    
    def skip_whitespace(self):
        if self.pos >= len(self.input):
            return
        while self.input[self.pos] in [' ', '\t', '\n']:
            self.pos += 1

def lexing(contents: str) -> "the list of token":
    tokens = []
    lexer = Lexer(contents)
    while True:
        token = lexer.next_token()
        if token.type == TokenType.EOF:
            break
        tokens.append(token)
    return tokens
