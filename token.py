from enum import IntEnum, auto

class TokenType(IntEnum):
    NUMBER = auto()
    PLUS = auto()
    MINUS = auto()
    MULTIPLE = auto()
    DIVISION = auto()
    EOF = auto ()
    
    def string(self):
        if self == TokenType.NUMBER:
            return "NUMBER"
        elif self == TokenType.PLUS:
            return "PLUS"
        elif self == TokenType.MINUS:
            return "MINUS"
        elif self == TokenType.MULTIPLE:
            return "MULTIPLE"
        elif self == TokenType.DIVISION:
            return "DIVISION"
        else:
            return "EOF"


class Token:
    def __init__(self, ty: TokenType, literal: str):
        self.type = ty
        self.input = literal
        
    def string(self):
        literal = self.input if self.input != '\0' else 'EOF'
        return f"ty->{self.type.string()}\tinput->{literal}"