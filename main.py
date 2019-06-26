from token import Token, TokenType

if __name__ == '__main__':
    number = Token(TokenType.NUMBER, "30")
    print(f'Type->{number.type.string()}\tInput->{number.input}')