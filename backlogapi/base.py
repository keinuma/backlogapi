"""
Base class for Backlog all object
"""


class BacklogBase:
    """
    Base class is identified by id and class name
    """
    def __init__(self):
        self.id = None

    def __hash__(self):
        return hash(type(self).__name__) ^ hash(self.id)

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return hash(self) == hash(other)
        raise ValueError
