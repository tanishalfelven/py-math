from .node_value import NodeValue

"""
Represents an integer value
"""
class NumberValue(NodeValue):
    def __init__(self, number_value):
        NodeValue.__init__(self)
        self.value = number_value
        return