"""
A node represents a single value or operator, typically used in tandem with other nodes
to create equations and meaningful data.
"""
class Node:
    def __init__(self, value):
        self.value = value