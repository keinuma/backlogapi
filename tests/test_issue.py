from . import BaseBacklogTestCase
from backlogapi import Issue, BacklogBase
from .result.res_issues import *


class TestResourceIssue(BaseBacklogTestCase):
    def test_space_instance(self):
        self.response.json.return_value = issue_json
        issues = self.client.issue.all()
        self.check_object(issues, issue_json)

    def test_issues_class_instance(self):
        self.response.json.return_value = issue_json
        issues = [Issue(self.client).from_json(res) for res in issue_json]
        self.check_object(issues, issue_json)

    def test_issues_url(self):
        self.assertEqual(self.client.issue.url, 'https://spaceName.backlog.jp/api/v2/issues')

    def test_issues_crud_function(self):
        # issues object have only get method
        for func in BacklogBase._crud_func:
            self.assertTrue(hasattr(self.client.issue, func))

    def test_issue_count(self):
        self.response.json.return_value = {'count': 12}
        count = self.client.issue.get_count()
        self.assertEqual(count, 12)

    def test_issue_get_comment(self):
        self.response.json.return_value = issue_comment_json
        comment = self.client.issue.get_comments()
        self.check_object(comment, issue_comment_json)

    def test_issue_get_attachments(self):
        self.response.json.return_value = issue_attachments_json
        attachments = self.client.issue.get_attachments()
        self.check_object(attachments, issue_attachments_json)

    def test_issue_shared_files(self):
        self.response.json.return_value = []
        shared_files = self.client.issue.get_shared_files()
        self.check_object(shared_files, [])
