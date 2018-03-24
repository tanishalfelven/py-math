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
            return self.__binary_evaluation(value_1, value_2)

    def evaluate_as_unary(self, value):
        if self.is_unary:
            return self.__unary_evaluation(value)

class Operations:
    # Unary Functions
    @staticmethod
    def positive_unary(value_1):
        return value_1

    @staticmethod
    def negative_unary(value_1):
        return -value_1

    # Binary Functions
    @staticmethod
    def addition(value_1, value_2):
        return value_1 + value_2

    @staticmethod
    def subtraction(value_1, value_2):
        return value_1 - value_2

    @staticmethod
    def multiplication(value_1, value_2):
        return value_1 * value_2

    @staticmethod
    def division(value_1, value_2):
        return value_1 / value_2