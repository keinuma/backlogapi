"""
Backlog API Library errors
"""


class BaseBacklogError(Exception):
    """
    Base exception class for backlog exception
    """


class InternalError(BaseBacklogError):
    """
    Error due to program bug etc
    """
    super().__init__('Error due to program bug etc')


class LicenceError(BaseBacklogError):
    """
    This functin can not be used with licence
    """
    super().__init__('This function can not be used with license')


class LicenceExpiredError(BaseBacklogError):
    """
    Licence has already expired
    """
    super().__init__('Licence has already expired')


class AccessDeniedError(BaseBacklogError):
    """
    Access denied
    """
    super().__init__('Access denied')


class UnauthorizedOperationError(BaseBacklogError):
    """
    Unauthorized operation is invoked by the user
    """
    super().__init__('Unauthorized operation is invoked by the user')


class NoResourceError(BaseBacklogError):
    """
    Requested resource dose not exist
    """
    super().__init__('Requested resource dose not exist')


class InvalidRequestError(BaseBacklogError):
    """
    Request parameter is invalid
    """
    super().__init__('Request parameter is invalid')


class SpaceOverCapacityError(BaseBacklogError):
    """
    Space capacity limit exceeded
    """
    super().__init__('Space capacity limit exceeded')


class ResourceOverflowError(BaseBacklogError):
    """
    Resource capacity limit exceeded
    """
    super().__init__('Resource capacity limit exceeded')


class TooLargeFileError(BaseBacklogError):
    """
    File size exceeds limit
    """
    super().__init__('File size exceeds limit')


class AuthenticationError(BaseBacklogError):
    """
    Certification failed
    """
    super().__init__('Certification failed')
