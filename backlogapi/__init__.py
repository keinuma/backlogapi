"""
2018/02/02 numata
backlog APIのクライアントライブラリ
config.jsonからapi keyをロードして、requestを投げる
"""

import os
import json
import requests


class BacklogProperty(object):
    """
    Backlog API v2 class
    This class get backlog space name and user api key.
    """

    def __init__(self, space, api_key):
        self.api_key = '?apiKey={}'.format(api_key)
        self.base_endpoint = 'https://{}.backlog.jp/api/v2/'.format(space)

    def common(self, method, url, *,
               url_params=None,
               query_params=None,
               request_params=None):
        """
        :param str url: リクエストURL
        :param str method: リクエストメソッド
        :param dict url_params:
        :param dict query_params:
        :param dict request_params:
        """
        relative_path = url.format(**url_params)
        endpoint = os.path.join(self.base_endpoint, relative_path, self.api_key)
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        method = method.lower()

        if method == "get":
            response = requests.get(endpoint, params=query_params)
        elif method == "patch":
            response = requests.patch(
                endpoint, params=query_params,
                data=request_params, headers=headers
            )
        elif method == "post":
            response = requests.post(
                endpoint, params=query_params,
                data=request_params, headers=headers
            )
        elif method == 'delete':
            response = requests.delete(endpoint, data=request_params)
        else:
            raise Exception('Not This method')

        if response.status_code >= 400:
            raise Exception(response, response.text)

        if response.status_code == 204:
            return None
        return response.json()

    def _check_parameter(self, params, required):
        """ checking parameter type """
        key = params.keys()
        for req_word in required:
            if req_word not in key:
                raise Exception('Not input required parameter')

    def get_space(self):
        """ Get space information """
        return self.common('GET', 'space')

    def get_projects(self, input_query_params=None):
        """ Get projects """
        return self.common('GET', 'projects', query_params=input_query_params)

    def get_progect_info(self, projectIdOrKey):
        """ Get project information """
        return self.common('GET',
                           'projects/{projectIdOrKey}',
                           url_params={'projectIdOrKey': projectIdOrKey})

    def get_share_file(self, projectIdOrKey, path, input_query_params=None):
        """ Get project share file """
        if input_query_params is None:
            input_query_params = {}
        return self.common('GET',
                           'projects/{projectIdOrKey}/files/metadata/{path}',
                           url_params={'projectIdOrKey': projectIdOrKey,
                                       'path': path},
                           query_params=input_query_params)

    def get_issues(self, input_query_params=None):
        """ Get issues """
        if input_query_params is None:
            input_query_params = {}
        return self.common('GET',
                           'issues',
                           query_params=input_query_params)

    def add_issues(self, input_request_params):
        """ Add issue """
        required_key = ['projectId', 'summary', 'issueTypeId', 'priorityId']
        self._check_parameter(required_key)
        return self.common('POST',
                           'issues',
                           request_params=input_request_params)

    def update_issue(self, issueIdOrKey, input_request_params=None):
        """ Update issue """
        if input_request_params is None:
            input_request_params = {}
        return self.common('PATCH',
                           'issues/{issueIdOrKey}',
                           url_params={'issueIdOrKey': issueIdOrKey},
                           request_params=input_request_params)

    def get_issue_attachments(self, issueIdOrKey):
        """ Get issue attachments """
        return self.common('GET',
                           'issues/{issueIdOrKey}/attachments',
                           url_params={'issueIdOrKey': issueIdOrKey})

    def delete_issue_attachments(self, issueIdOrKey, attachmentId):
        """ Delete issue attachments"""
        return self.common('DELETE',
                           'issues/{issueIdOrKey}/attachments/{attachmentId}',
                           url_params={'issueIdOrKey': issueIdOrKey,
                                       'attachmentId': attachmentId})

    # Admin User functions
    def get_space_capacity(self):
        """ Get space capacity """
        return self.common('GET', 'space/diskUsage')

    def get_users(self):
        """ Get user list """
        return self.common('GET', 'users')

    def add_user(self, input_request_params):
        """ Add user """
        required_key = ['userId', 'password', 'name',
                        'mailAddress', 'roleType']
        self._check_parameter(required_key)
        return self.common('POST', 'users',
                           request_params=input_request_params)

    def delete_user(self, userId):
        """ Delete user"""
        return self.common('DELETE',
                           'users/{userId}',
                           url_params={'userId': userId})

    def add_project(self, input_request_params):
        """ Add project """
        required_key = ['name', 'key', 'chartEnabled',
                        'projectLeaderCanEditProjectLeader',
                        'subtaskingEnabled', 'textFormattingRule']
        self._check_parameter(required_key)
        return self.common('POST', 'projects',
                           request_params=input_request_params)

    def delete_project(self, projectIdOrKey):
        """ Delete project """
        return self.common('DELETE',
                           'projects/{projectIdOrKey}',
                           url_params={'projectIdOrKey': projectIdOrKey})

    def add_project_user(self, projectIdOrKey, input_request_params):
        """ Add project user """
        required_key = ['userId']
        self._check_parameter(required_key)
        return self.common('POST',
                           'projects/{projectIdOrKey}/users',
                           url_params={'projectIdOrKey': projectIdOrKey},
                           request_params=input_request_params)

    def delete_project_user(self, projectIdOrKey, input_request_params):
        """ Delete project user """
        required_key = ['userId']
        self._check_parameter(required_key)
        return self.common('DELETE',
                           'projects/{projectIdOrKey}/users',
                           url_params={'projectIdOrKey': projectIdOrKey},
                           request_params=input_request_params)

    def add_project_admin(self, projectIdOrKey, input_request_params):
        """ Add project admin user """
        required_key = ['userId']
        self._check_parameter(required_key)
        return self.common('POST',
                           'projects/{projectIdOrKey}/administrators',
                           url_params={'projectIdOrKey': projectIdOrKey},
                           request_params=input_request_params)

    def delete_project_admin(self, projectIdOrKey, input_request_params):
        """ Delete project admin user """
        required_key = ['userId']
        self._check_parameter(required_key)
        return self.common('DELETE',
                           'projects/{projectIdOrKey}/administrators',
                           url_params={'projectIdOrKey': projectIdOrKey},
                           request_params=input_request_params)

    def delete_issue(self, issueIdOrKey):
        """ Delete issue """
        return self.common('DELETE',
                           'issues/{issueIdOrKey}',
                           url_params={'issueIdOrKey': issueIdOrKey})

    # -------------------------------------------------------
    # Adding function
    # -------------------------------------------------------

    def get_all_issues(self, input_query_params=None):
        """ Get All issues id and name """
        if input_query_params is None:
            input_query_params = {}
        input_query_params['offset'] = 0
        while True:
            issues = self.get_issues(input_query_params)
            if len(issues) == 0:
                break
            input_query_params['offset'] += len(issues)
            for issue in issues:
                yield issue


def load_config(path=os.getcwd(), filename="config.json"):
    """
    :param str path: configファイルのpath
    :param str filename: configファイルの名前
    :return dict:
    """
    data = dict()
    file_path = os.path.join(path, filename)
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
    except IOError:
        Exception("No such json file.")

    if data is None:
        Exception("json file is empty.")
    if "space" in data.keys() or "api_key" in data.keys():
        return data
    else:
        Exception("json file do not have auth key.")
