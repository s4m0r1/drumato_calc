from lex import lexing, Lexer
import os
import sys

def get_contents_from_file(filename: str) -> str:
    if not os.path.exists(filename):
        print(
            f"warning: no such file '{filename}'\nread from cmdarg instead of file..."
        )
        return filename + '\x00'
    return open(filename, 'r').read()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Fatal error: no input files")
        sys.exit()
    print("--------input--------")
    contents = get_contents_from_file(sys.argv[1])
    print(contents)
    tokens = lexing(contents)
    print("--------tokens--------")
    [print(t.string()) for t in tokens]