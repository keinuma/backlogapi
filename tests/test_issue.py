from . import mock, BaseBacklogTestCase

from backlogapi import BacklogClient, Issue
from .result import issues


class TestResourceIssue(BaseBacklogTestCase):
    def test_client_access(self):
        issue_obj = self.client.issue
        self.assertTrue(hasattr(issue_obj, 'get'))
        self.assertTrue(hasattr(issue_obj, 'from_json'))
        self.assertEqual(self.client, issue_obj.client)

    def test_notification_instance(self):
        issue_obj = self.client.issue.all()
        self.assertTrue(isinstance(issue_obj, list))
