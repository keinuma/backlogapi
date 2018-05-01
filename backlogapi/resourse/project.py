"""
Model for Backlog projects
"""

from .base import BacklogBase
from .user import User
from .. import utilities


class Project(BacklogBase):
    """
    Representing Backlog user
    """
    def __init__(self, client):
        super().__init__(client)
        self._attr = (
            ('id', 'id'),
            ('project_key', 'projectKey'),
            ('name', 'name'),
            ('chart_enabled', 'chartEnabled'),
            ('subtasking_enabled', 'subtaskingEnabled'),
            ('project_leader_can_edit_project_leader', 'projectLeaderCanEditProjectLeader'),
            ('text_formatting_rule', 'textFormattingRule'),
            ('archived', 'archived')
        )

    def all(self, query_params=None):
        """
        Get all projects
        :return:
        """
        if not query_params:
            query_params = {'archived': None, 'all': 'false'}
        res = self.client.fetch_json('projects', method='GET', query_params=query_params)
        return [Project(self).from_json(p) for p in res]

    def activities(self, **params):
        """
        Get the project activities
        """
        if self.id is None:
            return None
        return self.client.fetch_json(uri_path=f'projects/{self.id}/activities',
                                      query_params=params)

    @property
    def users(self):
        """
        Add user the project
        """
        res = self.client.fetch_json(uri_path=f'projects/{self.id}/users')
        return [User(self.client).from_json(u) for u in res]

    def add_user(self, user_id):
        """
        Add user the project
        :param user_id:
        """
        self.client.fetch_json(uri_path=f'projects/{self.id}/users',
                               method='POST',
                               post_params={'userId': user_id})

    @utilities.protect((1,))
    def delete_user(self, user_id):
        """
        Delete user the project
        :param user_id:
        """
        self.client.fetch_json(uri_path=f'projects/{self.id}/users',
                               method='DELETE',
                               post_params={'userId': user_id})

    @property
    @utilities.protect((1,))
    def admins(self):
        """
        Get admin user the project
        """
        res = self.client.fetch_json(uri_path=f'projects/{self.id}/administrator')
        return [User(self.client).from_json(u) for u in res]

    @utilities.protect((1,))
    def add_admin(self, user_id):
        """
        Add admin user the project
        :param user_id:
        """
        res = self.client.fetch_json(uri_path=f'projects/{self.id}/administrator',
                                     method='POST',
                                     post_params={'userId': user_id})
        return User(self.client).from_json(res)

    @utilities.protect((1,))
    def delete_admin(self, user_id):
        """
        Delete admin user the project
        :param user_id:
        """
        res = self.client.fetch_json(uri_path=f'projects/{self.id}/administrator',
                                     method='DELETE',
                                     post_params={'userId': user_id})
        return User(self.client).from_json(res)

    @property
    def issue_types(self):
        """
        Get issue type fpr the project
        """
        res = self.client.fetch_json(uri_path=f'projects/{self.id}/issueTypes')
        return [IssueType(self.client).from_json(i) for i in res]


class IssueType(BacklogBase):
    """
    Representing Project Issue type
    """
    def __init__(self, client):
        super().__init__(client)
        self._attr = (
            ('id', 'id'),
            ('project_id', 'projectId'),
            ('name', 'name'),
            ('color', 'color'),
            ('display_order', 'displayOrder'),
        )
