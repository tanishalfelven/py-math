from .operator import Operator
from .operator import Operations
from .parser_exception import ParserException
from .node import Node
from .number_value import NumberValue
from .operator import Operator

class Parser:
    def __init__(self):
        self.operators = []
        self.operator_representations = []
        self.max_precedence_level = 0
        self.__define_operator(Operator('+', 1, True, True, unary_evaluation=Operations.positive_unary, binary_evaluation = Operations.addition))
        self.__define_operator(Operator('-', 1, True, True, unary_evaluation=Operations.negative_unary, binary_evaluation = Operations.subtraction))
        self.__define_operator(Operator('*', 2, False, True, binary_evaluation = Operations.multiplication))
        self.__define_operator(Operator('/', 2, False, True, binary_evaluation = Operations.division))
        return

    def __define_operator(self, operator):
        self.operators.append(operator)
        self.operator_representations.append(operator.representation)
        # keep track of the maximum precedence level so when nodes are evaluated we don't skip any
        if operator.precedence_level > self.max_precedence_level:
            self.max_precedence_level = operator.precedence_level

    def get_operator_instance(self, representation):
        for operator in self.operators:
            if operator.representation == representation:
                return operator
        raise ParserException('Operator [' + representation + '] is not defined.')

    """
        Left-to-right, take numbers and operators and define them as nodes.
    """
    def create_nodes(self, input_string):
        nodes = []
        input_string = "".join(input_string.split()) # remove all whitespace in string
        node_string = ''
        for index, character in enumerate(input_string):
            is_end_of_input = len(input_string) == index+1
            parse_node_string_as_number = self.is_valid_number_string(character, node_string)
            node_string += character
            if parse_node_string_as_number:
                if is_end_of_input or not self.is_valid_number_string(input_string[index + 1], node_string):
                    nodes.append(Node(NumberValue(node_string)))
                    node_string = ''
            else:
                if is_end_of_input or self.is_valid_number_string(input_string[index + 1], node_string):
                    if node_string in self.operator_representations:
                        nodes.append(Node(self.get_operator_instance(node_string)))
                        node_string = ''
                    else:
                        raise ParserException('Unexpected sequence [' + node_string + ']')
        return nodes

    def is_valid_number_string(self, character, number_string_to_append_to):
        return character.isdigit() or character == '.' and '.' not in number_string_to_append_to

    def evaluate_nodes(self, nodes):
        return False

    def evaluate(self, input):
        nodes = self.create_nodes(input)
        result = self.evaluate_nodes(nodes)
        return result

