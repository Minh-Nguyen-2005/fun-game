# Author: Minh Nguyen
# Date: 11/08/2023
# Purpose: Vertex class

class Vertex:
    # A Vertex contains reference to a Python list of strings describing the connected vertices, and some data.
    # For the example vertex, the adjacency list would be ["LESS_TRAVELED", "BRIDGE"],
    # and the data would be "You are walking...more-traveled?"
    def __init__(self, adjacent, data):
        self.adjacent = adjacent
        self.data = data