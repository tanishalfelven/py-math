## Py Math Interpreter

Requirements
> Pluto is passionate about unit testing, Test Driven Development (TDD), pair programming, and writing clean production code. We want you to write a simple calculator with the following requirements:
> - Use the programming language you think you can do the best job with
> - Unit tested
> - Document any necessary frameworks/dependencies in some form of readme
> - Respects order of operations (PEMDAS)
> - A GUI is not required, just an interactive shell
> - Whitespace in input is ignored
> - Supports the following operators:
> - +, -, *, and /
> - Q for quit
> - = for evaluate
> 
> Designed in such a way that it would be easy to add additional operators
> Here are some calculations we will expect of your program:
> - 2+2 = 4
> - -5* 5/3 = -8.3333333333333333
> - 7+-6 = 1
> - -5* 5-15 /3 = -30

#### Approach and Planning
1. Take samples and put into unit tests. Throw some of my own in for spice.
2. Start the parsing (the fun part, parsing data like this is pretty fun to iron out)
    - Take input string ("2+2") and interpret out nodes that represent operators and values. Couple tricky things here, we need to adhere to PEMDAS and we need to watch out for unary operators 
        + \+ or - in front of a number that does not have a number on the other side need to evaluate as a value not an operation. 
            * My thinking is that we can simply have a flag for binary and unary operators when we define the operators. ()
        + In order to follow PEMDAS, let's first split all of our data into nodes and then we can simply iterate over the data left to right. Lets give operators a number value of precedence, lowest precedence being a value of 1 (for + and -) and highest precendence being 2 (for / and *). We will run through our interpreted string for as many levels of precende are currently defined (when defining operators we can simply have a levels_of_precedence variable). Hopefully this approach will future proof a little bit for '(' and ')' or other unforseen operators.
    - Evaluate data based on nodes.
        + The developer will only ever have to interact with a 'parser' object, where they will instantiate it then 'parser.eval(input).' Black box methodology.
    - Return result.
