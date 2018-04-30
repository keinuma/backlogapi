"""
Base class for Backlog all object
"""


class BacklogBase:
    """
    Base class is identified by id and class name
    """
    def __init__(self, client):
        self.client = client
        self.id = None
        self.name = None
        self._attr = None

    def __repr__(self):
        return f'<{self.__class__.__name__}:{self.name}>'

    def __hash__(self):
        return hash(type(self).__name__) ^ hash(self.id)

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return hash(self) == hash(other)
        raise NotImplementedError

    def from_json(self, response):
        """
        Create the Object by json response
        :param dict response: Space json object
        :return Space space: self
        """
        for key, res in self._attr:
            setattr(self, key, response.get(res, None))
        return self
