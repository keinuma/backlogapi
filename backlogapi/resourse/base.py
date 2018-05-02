"""
Base class for Backlog all object
"""


class BacklogBase:
    """
    Base class is identified by id and class name
    """
    endpoint = None

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

    def all(self):
        """
        Get all object
        """
        res = self.client.fetch_json(self.endpoint, method='GET')
        return [self.__class__(self.client).from_json(x) for x in res]

    def get(self, id_):
        """
        Get one object
        """
        res = self.client.fetch_json('/'.join([self.endpoint, id_]), method='GET')
        return self.__class__(self.client).from_json(res)

    def filter(self, **params):
        """
        Get filtering object
        :return:
        """
        res = self.client.fetch_json(self.endpoint, method='GET', query_params=params)
        return [self.__class__(self.client).from_json(x) for x in res]

    def create(self, **params):
        """
        Create new object
        """
        res = self.client.fetch_json(self.endpoint, method='POST', post_params=params)
        return self.__class__(self.client).from_json(res)

    def update(self, id_=None, **params):
        """
        Update the object
        """
        if self.id is not None:
            res = self.client.fetch_json(f'{self.endpoint}/{self.id}', method='POST', post_params=params)
        else:
            res = self.client.fetch_json(f'{self.endpoint}/{id_}', method='POST', post_params=params)
        return self.__class__(self.client).from_json(res)

    def delete(self, id_=None):
        if self.id is not None:
            res = self.client.fetch_json(f'{self.endpoint}/{self.id}', method='DELETE')
        else:
            res = self.client.fetch_json(f'{self.endpoint}/{id_}', method='DELETE')
        return self.__class__(self.client).from_json(res)

