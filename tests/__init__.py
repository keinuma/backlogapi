import os
import re
import unittest
from unittest import mock

import backlogapi
from backlogapi import BacklogClient


class BaseBacklogTestCase(unittest.TestCase):
    patch_prefix = 'patch'
    patch_targets = {'requests': 'backlogapi.backlogclient.requests.request'}

    def setUp(self):
        self.client = BacklogClient('apiKey', 'spaceName')
        self.client.role = 1
        self.response = mock.MagicMock(status_code=200, history=[], method='GET')
        for target, path in self.patch_targets.items():
            setattr(self, f'{self.patch_prefix}_{target}',
                    mock.patch(path, return_value=self.response).start())
        self.addCleanup(mock.patch.stopall)

    def set_patch_side_effect(self, side_effect):
        for target in self.patch_targets:
            getattr(self, f'{self.patch_prefix}_{target}').side_effect = side_effect

    def check_object(self, instance, response: dict):
        """
        Check attribution in instance object equal response
        :param instance:
        :param dict response:
        :return:
        """
        if isinstance(response, list):
            if response:
                response = response[0]
                instance = instance[0]
            else:
                self.assertEqual(instance, response)
                return None

        for key in response.keys():
            if key in ('nulabAccount',):
                continue
            snake_key = self.camel_to_snake(key)
            value = getattr(instance, snake_key, None)
            if value and 'backlogapi' in str(type(value)):
                self.check_object(value, response[key])
                continue
            self.assertEqual(value, response[key])

    def camel_to_snake(self, string):
        return re.sub("([A-Z])", lambda x: "_" + x.group(1).lower(), string)