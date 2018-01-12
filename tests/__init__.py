import unittest
from backlogapi import BacklogProperty


class TestBacklogProperty(unittest.TestCase):
    ''' backlog api test by unittest'''

    def test_init(self):
        client = BacklogProperty('pyphysics', 'NkP4irvkHOXAsvFL4kJZlaBSrkoK8x1plBS87FINIx2j6Kw31nhHa06AN9ghpAIY')
        self.assertEqual(client.space, 'pyphysics')
        self.assertEqual(client.api_key, 'NkP4irvkHOXAsvFL4kJZlaBSrkoK8x1plBS87FINIx2j6Kw31nhHa06AN9ghpAIY')
        self.assertEqual(client.base_endpoint, 'https://pyphysics.backlog.jp/api/v2')

    def test_check_parameter(self):
        testing = {'name': 'numata', 'python': 'all'}
        required = ['name', 'python']
        self.assertEqual(BacklogProperty.check_parameter(testing, required), '')
