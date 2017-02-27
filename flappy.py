# Created by Mihai Sandor & Dobai David
import sys

from core.flappy_parser import *
from lexer.flappy_lexer import *


def usage():
    sys.stderr.write('Usage: flappylang filename\n')
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
    filename = sys.argv[1]
    text = open(filename).read()
    tokens = flappy_lex(text)
    parse_result = flappy_parse(tokens)
    if not parse_result:
        sys.stderr.write('Parse error!\n')
        sys.exit(1)
    ast = parse_result.value
    env = {}
    ast.eval(env)

    sys.stdout.write('Final variable values:\n')
    for name in env:
        sys.stdout.write('%s: %s\n' % (name, env[name]))
