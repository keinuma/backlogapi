from unittest import mock

from . import BaseBacklogTestCase
from backlogapi import BacklogClient, Space, BacklogBase
from .result.res_space import space_json, activate_json, disk_usage_json


class TestResourceSpace(BaseBacklogTestCase):
    def test_space_instance(self):
        self.response.json.return_value = space_json
        space = self.client.space.get()
        self.check_object(space, space_json)

    def test_space_url(self):
        self.assertEqual(self.client.space.url, 'https://spaceName.backlog.jp/api/v2/space')

    def test_space_crud_function(self):
        # space object have only get method
        for func in BacklogBase._crud_func:
            if func == 'get':
                self.assertTrue(hasattr(self.client.space, func))
            else:
                self.assertFalse(hasattr(self.client.space, func))

    def test_space_activities(self):
        self.response.json.return_value = activate_json
        activities = self.client.space.get_activities()
        self.assertEqual(activities[0]['id'], activate_json[0]['id'])

    def test_space_get_notification(self):
        self.response.json.return_value = {
            "content": "Notification",
            "updated": "2018-05-01T01:21:11Z"
        }
        notification = self.client.space.get_notification()
        self.assertEqual(notification['content'], 'Notification')

    def test_update_notification(self):
        self.response.json.return_value = {
            "content": "Notification",
            "updated": "2018-05-01T01:21:11Z"
        }
        notification = self.client.space.update_notification()
        self.assertEqual(notification['content'], 'Notification')

    def test_get_disk_usage(self):
        self.response.json.return_value = disk_usage_json
        disk_usage = self.client.space.get_disk_usage()
        self.assertEqual(disk_usage['capacity'], disk_usage_json['capacity'])
