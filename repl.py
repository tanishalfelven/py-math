from parser.parser import Parser

def main():
    print('------------------------------')
    print('-Welcome to PyMath Calculator-')
    print('------------------------------')
    print('https://github.com/tanishalfelven/pymath')
    print("When the '>' appears enter any math equation (decimals and +-*/)\nand press enter to have it evaluated.")
    print("Press 'Q' to quit.")
    parser = Parser()
    while True:
        user_input = input('> ')
        if user_input.upper() == 'Q':
            print('goodbye!')
            break
        else:
            print('= %s' % (parser.evaluate(user_input)))

if __name__ == "__main__":main()