import os
import unittest
from unittest import mock

from backlogapi import BacklogClient


class BaseBacklogTestCase(unittest.TestCase):
    def setUp(self):
        self.client = BacklogClient(api_key=os.getenv('BACKLOG_API_KEY'),
                                    space_name=os.getenv('BACKLOG_SPACE'))
        response = mock.Mock(status_code=200, history=[])
