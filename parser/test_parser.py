import unittest
from .parser import Parser
from .node import Node
from .number_value import NumberValue
from .operator import Operator

"""
    There are two things main elements of ensuring the parser works as expected:
        1. Node creation. This is the first step of the parser, we need to ensure
        that the Nodes that are generated from input match the expected created nodes.
        2. Order of Operations being correctly implemented into the parser. (4+3*2 = 10 not 14 or something else)
    
    Provided Test Cases
    > - 2+2 = 4
    > - -5* 5/3 = -8.3333333333333333
    > - 7+-6 = 1
    > - -5* 5-15 /3 = -30
"""

class ParserTestCase(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()

    def test_create_nodes(self):
        self.assertEqual(self.parser.create_nodes('2+2'), [
            Node(NumberValue(2)),
            Node(self.parser.get_operator_instance('+')),
            Node(NumberValue(2))
        ])

        self.assertEqual(self.parser.create_nodes('-5* 5/3'), [
            Node(self.parser.get_operator_instance('-')),
            Node(NumberValue(5)),
            Node(self.parser.get_operator_instance('*')),
            Node(NumberValue(5)),
            Node(self.parser.get_operator_instance('/')),
            Node(NumberValue(3))
        ])
        self.assertEqual(self.parser.create_nodes('7+-6'), [
            Node(NumberValue(7)),
            Node(self.parser.get_operator_instance('+')),
            Node(self.parser.get_operator_instance('-')),
            Node(NumberValue(6)),
        ])
        self.assertEqual(self.parser.create_nodes('-5* 5-15 /3'), [
            Node(self.parser.get_operator_instance('-')),
            Node(NumberValue(5)),
            Node(self.parser.get_operator_instance('*')),
            Node(NumberValue(5)),
            Node(self.parser.get_operator_instance('-')),
            Node(NumberValue(15)),
            Node(self.parser.get_operator_instance('/')),
            Node(NumberValue(3))
        ])

    def test_evaulate(self):
        self.assertEqual(self.parser.evaluate('2+2'), 4)
        self.assertEqual(self.parser.evaluate('-5* 5/3'), -25/3)
        self.assertEqual(self.parser.evaluate('7+-6'), 1)
        self.assertEqual(self.parser.evaluate('-5* 5-15 /3'), -30)

if __name__ == '__main__':
    unittest.main()
