"""
Backlog Client object
"""

import os
import json
import requests

from space import Space


class BacklogClient:
    """Backlog API"""

    def __init__(self, api_key, space_name):
        """
        Backlog api client
        :param str api_key: API key
        :param str space_name: Backlog space
        """
        self._api_key = api_key
        self._space_name = space_name
        self.model_endpoint = f'https://{self._space_name}.backlog.jp/api/v2/'

    def fetch_json(self, uri_path, method='GET', headers=None, query_params=None, post_params=None, files=None):
        """
        Making request by this function arguments
        :param str uri_path: uri path continue endpoint
        :param str method: request method
        :param str headers: request headers
        :param dict query_params: query parameter
        :param dict post_params: base of data
        :param files:
        """
        if headers is None:
            headers = {}
        if query_params is None:
            query_params = {}
        if post_params is None:
            post_params = {}
        query_params['apiKey'] = self._api_key

        data = None
        if files is None:
            data = json.dumps(post_params)

        if method.upper() in ('POST', 'PUT', 'DELETE') and files is not None:
            headers['Content-Type'] = 'application/json; charset=utf8'
        headers['Accept'] = 'application/json'

        if uri_path.startswith('/'):
            uri_path = uri_path[1:]
        url = self.model_endpoint + uri_path
        print(url)

        response = requests.request(method=method, url=url, params=query_params, headers=headers,
                                    data=data, files=files)

        if response.status_code >= 400:
            raise Exception(response, response.text)
        elif response.status_code == 204:
            return None

        return response.json()

    def get_space(self):
        """
        Get space information
        :return:
        """
        res = self.fetch_json('space', method='GET')
        return Space.from_json(self, res)
