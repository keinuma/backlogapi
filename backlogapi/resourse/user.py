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
            ('role_type', 'roleType'),
            ('lang', 'lang'),
            ('mail_address', 'mailAddress')
        )

    @property
    def watching(self):
        res = self.client.fetch_json(uri_path=f'users/{self.id}/watchings')
        for x in res:
            x['user_id'] = self.id
        return [Watching(self.client).from_json(r) for r in res]


class Watching(BacklogBase):
    """
    Representing Backlog user watching
    """

    def __init__(self, client):
        super().__init__(client)
        self.user_id = None
        self._attr = (
            ('id', 'id'),
            ('resource_already_read', 'resourceAlreadyRead'),
            ('note', 'note'),
            ('type', 'type'),
            ('_issue', 'issue'),
            ('last_content_updated', 'lastContentUpdated'),
            ('created', 'created'),
            ('updated', 'updated'),
            ('user_id', 'user_id'),
        )

    def from_json(self, response):
        from . import Issue
        res = super().from_json(response)
        setattr(self, 'endpoint', f'users/{self.user_id}/watchings')
        setattr(self, 'issue', Issue(self.client).from_json(res['_issue']))
        return self
