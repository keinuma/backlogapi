"""
Helper function for Backlog API
"""


from functools import wraps

from . import exceptions


def protect(roles):
    def _protect(func):
        @wraps(func)
        def __protect(self, *args, **kwargs):
            print(self.client.role, roles)
            if self.client.role not in roles:
                raise exceptions.UnauthorizedOperationError
            return func(self, *args, **kwargs)
        return __protect
    return _protect
