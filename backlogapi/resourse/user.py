"""
Model for Backlog user
"""

from .base import BacklogBase
from .. import utilities


class User(BacklogBase):
    """
    Representing Backlog user
    """
    endpoint = 'users'

    def __init__(self, client):
        super().__init__(client)
        self._attr = (
            ('id', 'id'),
            ('user_id', 'userId'),
            ('name', 'name'),
            ('roleType', 'roleType'),
            ('lang', 'lang'),
            ('mail_address', 'mailAddress')
        )
