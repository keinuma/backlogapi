"""
Model for Backlog projects
"""

from .base import BacklogBase
from .project import IssueType, Version
from .shared_file import SharedFile
from .star import Star
from .. import utilities


class Issue(BacklogBase):
    """
    Representing issue
    """

    endpoint = 'issues'

    def __init__(self, client):
        super().__init__(client)
        self.issue_type = None
        self.created_user = None
        self.updated_user = None
        self._attr = (
            ('id', 'id'),
            ('project_id', 'projectId'),
            ('issue_key', 'issueKey'),
            ('key_id', 'keiId'),
            ('_issue_type', 'issueType'),
            ('summary', 'summary'),
            ('description', 'description'),
            ('resolutions', 'resolutions'),
            ('_priority', 'priority'),
            ('_status', 'status'),
            ('_assignee', 'assignee'),
            ('category', 'category'),
            ('versions', 'versions'),
            ('_milestone', 'milestone'),
            ('start_date', 'startDate'),
            ('due_date', 'dueDate'),
            ('estimated_hours', 'estimatedHours'),
            ('actual_hours', 'actualHours'),
            ('parent_issue_id', 'parentIssueId'),
            ('_created_user', 'createdUser'),
            ('created', 'created'),
            ('_updated_user', 'updatedUser'),
            ('updated', 'updated'),
            ('custom_fields', 'customFields'),
            ('_attachments', 'attachments'),
            ('_shared_files', 'sharedFiles'),
            ('_stars', 'stars'),
        )

    @property
    def count(self, **params):
        """
        Get issue counts
        :return:
        """
        res = self.client.fetch_json(uri_path='issues/count', query_params=params)
        return res['count']

    @property
    def comments(self):
        """
        Get issue comments  for the project
        """
        res = self.client.fetch_json(uri_path=f'issues/{self.id}/comments')
        for x in res:
            x['issue_id'] = self.id
        return [IssueComment(self.client).from_json(i) for i in res]

    @property
    def attachments(self):
        """
        Get issue attachments fields for the project
        """
        res = self.client.fetch_json(uri_path=f'issues/{self.id}/attachments')
        for x in res:
            x['issue_id'] = self.id
        return [IssueAttachment(self.client).from_json(i) for i in res]

    @property
    def shared_files(self):
        """
        Get issue shared fields for the project
        """
        res = self.client.fetch_json(uri_path=f'issues/{self.id}/sharedFiles')
        for x in res:
            x['issue_id'] = self.id
        return [IssueAttachment(self.client).from_json(i) for i in res]

    def link_shared_file(self, file_id):
        """
        Link the issue and shared file
        """
        res = self.client.fetch_json(uri_path=f'issues/{self.id}/sharedFiles',
                                     method='POST', post_params={'fileId': file_id})
        return IssueSharedFile(self).from_json(res)

    def from_json(self, response):
        from . import User
        res = super().from_json(response)
        setattr(self, 'issue_type', IssueType(self.client).from_json(res._issue_type))
        setattr(self, 'priority', Priority(self.client).from_json(res._priority))
        setattr(self, 'assignee', User(self.client).from_json(res._assignee))
        setattr(self, 'milestone', [Version(self.client).from_json(r) for r in res._milestone])
        setattr(self, 'created_user', User(self.client).from_json(res._created_user))
        setattr(self, 'updated_user', User(self.client).from_json(res._updated_user))
        if res._attachments != []:
            setattr(self, 'attachments', [IssueAttachment(self.client).from_json(r) for r in res._attachments])
        if res._shared_files != []:
            setattr(self, 'shared_files', [SharedFile(self.client).from_json(f) for f in res._shared_files])
        if res._stars != []:
            setattr(self, 'stars', [Star(self.client).from_json(f) for f in res._stars])
        return self


class Status(BacklogBase):
    """
    Representing issue status
    """
    endpoint = 'statuses'

    def __init__(self, client):
        super().__init__(client)
        self._attr = (
            ('id', 'id'),
            ('name', 'name'),
        )


class Resolution(BacklogBase):
    """
    Representing issue resolution
    """
    endpoint = 'resolutions'

    def __init__(self, client):
        super().__init__(client)
        self._attr = (
            ('id', 'id'),
            ('name', 'name'),
        )


class Priority(BacklogBase):
    """
    Representing issue priority
    """
    endpoint = 'resolutions'

    def __init__(self, client):
        super().__init__(client)
        self._attr = (
            ('id', 'id'),
            ('name', 'name'),
        )


class IssueComment(BacklogBase):
    """
    Representing issue comment
    """

    def __init__(self, client):
        super().__init__(client)
        self.issue_id = None
        self._attr = (
            ('id', 'id'),
            ('content', 'content'),
            ('change_log', 'changeLog'),
            ('_created_user', 'createdUser'),
            ('created', 'created'),
            ('updated', 'updated'),
            ('stars', 'stars'),
            ('notifications', 'notifications'),
            ('issue_id', 'issue_id'),
        )

    def from_json(self, response):
        from . import User
        res = super().from_json(response)
        setattr(self, 'endpoint', f'issues/{self.issue_id}/comments')
        setattr(self, 'created_user', User(self.client).from_json(res._created_user))
        return self

    @property
    def count(self, **params):
        """
        Get issue comments counts
        :return:
        """
        res = self.client.fetch_json(uri_path=f'issues/{self.id}/comments/count', query_params=params)
        return res['count']


class IssueAttachment(BacklogBase):
    """
    Representing issue attachment
    """

    def __init__(self, client):
        super().__init__(client)
        self.issue_id = None
        self._attr = (
            ('id', 'id'),
            ('name', 'name'),
            ('size', 'size'),
            ('_created_user', 'createdUser'),
            ('created', 'created'),
        )

    def from_json(self, response):
        from . import User
        res = super().from_json(response)
        setattr(self, 'endpoint', f'issues/{self.issue_id}/attachments')
        if hasattr(res, '_created_user'):
            setattr(self, 'created_user', User(self.client).from_json(res._created_user))
        return self


class IssueSharedFile(BacklogBase):
    """
    Representing issue shared file
    """

    def __init__(self, client):
        super().__init__(client)
        self.issue_id = None
        self._attr = (
            ('id', 'id'),
            ('type', 'type'),
            ('dir', 'dir'),
            ('name', 'name'),
            ('size', 'size'),
            ('_created_user', 'createdUser'),
            ('created', 'created'),
            ('_updated_user', 'updatedUser'),
            ('updated', 'updated'),
            ('issue_id', 'issue_id'),
        )

    def from_json(self, response):
        from . import User
        res = super().from_json(response)
        setattr(self, 'endpoint', f'issues/{self.issue_id}/sharedFiles')
        setattr(self, 'created_user', User(self.client).from_json(res._created_user))
        setattr(self, 'updated_user', User(self.client).from_json(res._updated_user))
        return self

    def download(self):
        """
        Download shared file the issue
        """
        self.client.fetch_json(uri_path=f'projects/{self.issue_id}/files/{self.id}')
        return self

    def link_issue(self, issue_id):
        """
        Link issue and the shared file
        """
        res = self.client.fetch_json(uri_path=f'issues/{issue_id}/sharedFiles',
                                     method='POST', post_params={'fileId': self.id})
        return IssueSharedFile(self.client).from_json(res)
