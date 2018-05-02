"""
Helper function for Backlog API
"""


from functools import wraps

from . import exceptions


def protect(roles):
    def _protect(func):
        @wraps(func)
        def __protect(self, *args, **kwargs):
            if self.__class__.__name__ == 'BacklogClient':
                role = self.role
            else:
                role = self.client.role
            if role not in roles:
                raise exceptions.UnauthorizedOperationError
            return func(self, *args, **kwargs)
        return __protect
    return _protect
