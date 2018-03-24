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
                if is_end_of_input or self.is_valid_number_string(input_string[index + 1], node_string) or node_string in self.operator_representations:
                    if node_string in self.operator_representations:
                        nodes.append(Node(self.get_operator_instance(node_string)))
                        node_string = ''
                    else:
                        raise ParserException('Unexpected sequence [' + node_string + ']')
        return nodes

    def is_valid_number_string(self, character, number_string_to_append_to):
        return character.isdigit() or character == '.' and '.' not in number_string_to_append_to

    def evaluate_nodes(self, nodes):
        for precedence_level in range(self.max_precedence_level, 0, -1):
            index = 0
            while self.nodes_has_operators_of_precedence(precedence_level, nodes):
                if not nodes[index].value.is_value \
                        and precedence_level == nodes[index].value.precedence_level \
                        and nodes[index].value.is_binary \
                        and index != 0:
                    changes = self.get_evaluation_of_binary_expression_at(index, nodes)
                    nodes = nodes[:changes['begin']] + [Node(NumberValue(changes['value']))] + nodes[changes['end']:]
                    if len(nodes) > 1:
                        index = 0
                        continue
                index+=1
        return nodes[0].value.value

    def nodes_has_operators_of_precedence(self, precedence, nodes):
        for node in nodes:
            if not node.value.is_value and precedence == node.value.precedence_level:
                return True
        return False

    def get_evaluation_of_binary_expression_at(self, index_of_operator, nodes):
        beginning_index = None
        for index in range(index_of_operator-1, -1, -1):
            if nodes[index].value.is_value and index != index_of_operator-1:
                beginning_index = index + 2
                break
            elif index == 0:
                beginning_index = 0
                break

        if beginning_index < index_of_operator:
            value1 = self.evaluate_unary_expression(nodes[beginning_index:index_of_operator])

        ending_index = None
        for index in range(index_of_operator+1, len(nodes)):
            if index == len(nodes)-1 or nodes[index].value.is_value:
                ending_index = index+1
                break

        if ending_index == index_of_operator + 1:
            value2 = nodes[ending_index].value.value
        else:
            value2 = self.evaluate_unary_expression(nodes[index_of_operator+1:ending_index])

        value = nodes[index_of_operator].value.evaluate_as_binary(value1, value2)
        return {'begin': beginning_index, 'end':ending_index, 'value': value}

    """
        Expects a list of nodes where the rightmost is a NumberValue
        and all other nodes are unary operators.
    """
    def evaluate_unary_expression(self, nodes):
        value = nodes[-1].value.value
        for index in range(len(nodes)-2, -1, -1):
            if not nodes[index].value.is_value:
                if nodes[index].value.is_unary:
                    value = nodes[index].value.evaluate_as_unary(value)
                else:
                    raise ParserException('Expected unary operator, found [' + nodes[index].value.representation + ']')
            else:
                raise ParserException('Expected unary operator, found number value [' + nodes[index].value.value + ']')
        return value

    def evaluate(self, input):
        nodes = self.create_nodes(input)
        result = self.evaluate_nodes(nodes)
        return result

