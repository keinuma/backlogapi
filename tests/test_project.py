from . import BaseBacklogTestCase
from backlogapi import Project, BacklogBase
from .result.res_project import *


class TestResourceSpace(BaseBacklogTestCase):
    def test_space_instance(self):
        self.response.json.return_value = project_json
        projects = self.client.project.all()
        self.check_object(projects, project_json)

    def test_projects_class_instance(self):
        self.response.json.return_value = project_json
        projects = [Project(self.client).from_json(res) for res in project_json]
        self.check_object(projects, project_json)

    def test_projects_url(self):
        self.assertEqual(self.client.project.url, 'https://spaceName.backlog.jp/api/v2/projects')

    def test_projects_crud_function(self):
        # projects object have only get method
        for func in BacklogBase._crud_func:
            self.assertTrue(hasattr(self.client.project, func))

    def test_project_users(self):
        self.response.json.return_value = users_json
        users = self.client.project.all()[0].get_users()
        self.check_object(users, users_json)

    def test_project_admins(self):
        self.response.json.return_value = admins_json
        admins = self.client.project.get_admins()
        self.check_object(admins, admins_json)

    def test_projects_activities(self):
        self.response.json.return_value = activities_json
        activities = self.client.project.all()[0].get_activities()
        print(activities)
        self.assertEqual(activities[0]['id'], activities_json[0]['id'])

    def test_project_issue_types(self):
        self.response.json.return_value = issue_types_json
        issue_types = self.client.project.all()[0].issue_types
        self.check_object(issue_types, issue_types_json)

    def test_project_categories(self):
        self.response.json.return_value = categories_json
        categories = self.client.project.all()[0].categories
        self.check_object(categories, categories_json)

    def test_project_versions(self):
        self.response.json.return_value = versions_json
        versions = self.client.project.all()[0].versions
        self.check_object(versions, versions_json)

    def test_project_shared_files(self):
        self.response.json.return_value = shared_files_json
        shared_files = self.client.project.all()[0].shared_files
        self.check_object(shared_files, shared_files_json)

    def test_project_webhooks(self):
        self.response.json.return_value = webhooks_json
        webhooks = self.client.project.all()[0].webhooks
        self.check_object(webhooks, webhooks_json)
