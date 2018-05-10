from backlogapi import User, BacklogBase
from . import BaseBacklogTestCase
from .result import res_user


class TestResourceUser(BaseBacklogTestCase):
    def test_user_all_method(self):
        self.response.json.return_value = res_user.users_json
        users = self.client.user.all()
        self.check_object(users, res_user.users_json)

    def test_user_all_method_class(self):
        self.response.json.return_value = res_user.users_json
        users = User(self.client).all()
        self.check_object(users, res_user.users_json)

    def test_user_url(self):
        self.assertEqual(self.client.user.url, 'https://spaceName.backlog.jp/api/v2/users')

    def test_user_get_method(self):
        self.response.json.return_value = res_user.user_json
        user = self.client.user.get(144217)
        self.check_object(user, res_user.user_json)

    def test_user_create_method(self):
        pass

    def test_user_crud_func(self):
        for func in BacklogBase._crud_func:
            if func == 'filter':
                self.assertFalse(hasattr(self.client.user, func))
            else:
                self.assertTrue(hasattr(self.client.user, func))
