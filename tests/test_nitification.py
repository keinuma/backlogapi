from . import mock, BaseBacklogTestCase

from backlogapi import BacklogClient, Notification
from .result import notifications


class TestResourceNotification(BaseBacklogTestCase):
    def test_client_access(self):
        notifications_obj = self.client.notification
        self.assertTrue(hasattr(notifications_obj, 'get'))
        self.assertTrue(hasattr(notifications_obj, 'from_json'))
        self.assertEqual(self.client, notifications_obj.client)

    def test_notification_instance(self):
        notifications_obj = self.client.notification.all()
        self.assertTrue(isinstance(notifications_obj, list))
