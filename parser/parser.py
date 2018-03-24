from .operator import Operator
from .operator import Operations
from .parser_exception import ParserException

class Parser:
    def __init__(self):
        self.operators = []
        self.max_precedence_level = 0
        self.__define_operator(Operator('+', 1, True, True, unary_evaluation=Operations.positive_unary, binary_evaluation = Operations.addition))
        self.__define_operator(Operator('-', 1, True, True, unary_evaluation=Operations.negative_unary, binary_evaluation = Operations.subtraction))
        self.__define_operator(Operator('*', 2, False, True, binary_evaluation = Operations.multiplication))
        self.__define_operator(Operator('/', 2, False, True, binary_evaluation = Operations.division))
        return

    def __define_operator(self, operator):
        self.operators.append(operator)
        # keep track of the maximum precedence level so when nodes are evaluated we don't skip any
        if operator.precedence_level > self.max_precedence_level:
            self.max_precedence_level = operator.precedence_level

    def get_operator_instance(self, representation):
        for operator in self.operators:
            if operator.representation == representation:
                return operator
        raise ParserException('Operator [' + representation + '] is not defined.')

    def create_nodes(self, input):
        return False

    def evaluate_nodes(self, nodes):
        return False

    def evaluate(self, input):
        nodes = self.create_nodes(input)
        result = self.evaluate_nodes(nodes)
        return result

