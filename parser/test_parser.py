import unittest
from parser.parser import Parser
from parser.parser_exception import ParserException
from parser.node import Node
from parser.number_value import NumberValue

"""
    There are two things main elements of ensuring the parser works as expected:
        1. Node creation. This is the first step of the parser, we need to ensure
        that the Nodes that are generated from input match the expected created nodes.
        2. Order of Operations being correctly implemented into the parser. (4+3*2 = 10 not 14 or something else)
"""

class ParserTestCase(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_create_nodes(self):
        nodes = self.parser.create_nodes('2+2')
        self.assertEqual(nodes[0].value.value, 2)
        self.assertEqual(nodes[1].value.representation, '+')
        self.assertEqual(nodes[2].value.value, 2)
        self.assertRaises(ParserException, self.parser.create_nodes, '???')
        nodes = self.parser.create_nodes('-5* 5-15 /3')
        self.assertEqual(nodes[0].value.representation, '-')
        self.assertEqual(nodes[1].value.value, 5)
        self.assertEqual(nodes[2].value.representation, '*')
        self.assertEqual(nodes[3].value.value, 5)
        self.assertEqual(nodes[4].value.representation, '-')
        self.assertEqual(nodes[5].value.value, 15)
        self.assertEqual(nodes[6].value.representation, '/')
        self.assertEqual(nodes[7].value.value, 3)
        nodes = self.parser.create_nodes('+-+-5')
        self.assertEqual(nodes[0].value.representation, '+')
        self.assertEqual(nodes[1].value.representation, '-')
        self.assertEqual(nodes[2].value.representation, '+')
        self.assertEqual(nodes[3].value.representation, '-')
        self.assertEqual(nodes[4].value.value, 5)
        nodes = self.parser.create_nodes('5.5+.3')
        self.assertEqual(nodes[0].value.value, 5.5)

    def test_evaluate_unary_expressions(self):
        nodes = self.parser.create_nodes('+-+-5')
        self.assertEqual(self.parser.evaluate_unary_expression(nodes), 5)
        nodes = self.parser.create_nodes('-5')
        self.assertEqual(self.parser.evaluate_unary_expression(nodes), -5)
        nodes = [Node(NumberValue(5))]
        self.assertEqual(self.parser.evaluate_unary_expression(nodes), 5)

    def test_get_evaluation_of_binary_expression_at(self):
        nodes = self.parser.create_nodes('6+-9')
        self.assertEqual(self.parser.get_evaluation_of_binary_expression_at(1, nodes), {'begin':0,'end':4,'value':-3})
        nodes = self.parser.create_nodes('-5+3*4')
        self.assertEqual(self.parser.get_evaluation_of_binary_expression_at(2, nodes), {'begin':0,'end':4,'value':-2})
        self.assertEqual(self.parser.get_evaluation_of_binary_expression_at(4, nodes), {'begin':3,'end':6,'value':12})

    def test_evaulate(self):
        self.assertEqual(self.parser.evaluate('2+2'), 4)
        self.assertEqual(self.parser.evaluate('-5* 5/3'), -25/3)
        self.assertEqual(self.parser.evaluate('7+-6'), 1)
        self.assertEqual(self.parser.evaluate('-5* 5-15 /3'), -30)

if __name__ == '__main__':
    unittest.main()
