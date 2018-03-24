from .number_value import NodeValue

class Operator(NodeValue):
    def __init__(self, representation, precedence_level, is_unary, is_binary, unary_evaluation = None, binary_evaluation = None):
        NodeValue.__init__(self)
        self.is_value = False
        self.representation = representation
        self.precedence_level = precedence_level
        self.is_unary = is_unary
        self.__unary_evaluation = unary_evaluation
        self.is_binary = is_binary
        self.__binary_evaluation = binary_evaluation

    def evaluate_as_binary(self, value_1, value_2):
        if self.is_binary:
            self.__binary_evaluation(value_1, value_2)

    def evaluate_as_unary(self, value):
        if self.is_unary:
            self.__unary_evaluation(value)
