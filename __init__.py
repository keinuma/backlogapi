import requests


class BacklogProperty(object):
    """
    Backlog API v2 class
    This class get backlog space name and user api key.
    """
    # Data member base url.
    org_endpoint = 'https://{space}.backlog.jp/api/v2/'
    api_format = '?apiKey={}'

    def __init__(self, space, api_key):
        self.space = space
        self.api_key = self.api_format.format(api_key)
        self.base_endpoint = self.org_endpoint.format(space=space)

    def common(self, method, url,
               url_params={}, query_params={}, request_params={}):
        '''
        method: requests method(get or post or delete)
        url_params: URL paramaters.
        query_params: method conditions.
        request_params: data for puts requests.
        '''
        relative_path = url.format(**url_params)
        endpoint = self.base_endpoint + relative_path + self.api_key
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        method = method.lower()

        if method == "get":
            response = requests.get(endpoint, params=query_params)
        elif method == "patch":
            response = requests.patch(
                endpoint, params=query_params,
                data=request_params, headers=headers)
        elif method == "post":
            response = requests.post(
                endpoint, params=query_params,
                data=request_params, headers=headers)
        elif method == 'delete':
            response = requests.delete(endpoint, data=request_params)
        else:
            raise Exception('Not This method')

        if response.status_code >= 400:
            raise Exception(response, response.text)

        if response.status_code == 204:
            return None

        return response.json()

    @staticmethod
    def check_parameter(params, required):
        """ checking parameter type """
        key = params.keys()
        for reqword in required:
            if reqword not in key:
                raise Exception('Not input required parameter')

    def get_space(self):
        ''' Get space information '''
        return self.common('GET', 'space')

    def get_projects(self, input_query_params=None):
        ''' Get projects '''
        return self.common('GET', 'projects', query_params=input_query_params)

    def get_progect_info(self, projectIdOrKey):
        ''' Get project information '''
        return self.common('GET',
                           'projects/{projectIdOrKey}',
                           url_params={'projectIdOrKey': projectIdOrKey})

    def get_sharefile(self, projectIdOrKey, path, input_query_params={}):
        ''' Get project share file '''
        return self.common('GET',
                           'projects/{projectIdOrKey}/files/metadata/{path}',
                           url_params={'projectIdOrKey': projectIdOrKey,
                                       'path': path},
                           query_params=input_query_params)

    def get_issues(self, input_query_params={}):
        ''' Get issues '''
        return self.common('GET',
                           'issues',
                           query_params=input_query_params)

    def add_issues(self, input_request_params):
        ''' Add issue '''
        required_key = ['projectId', 'summary', 'issueTypeId', 'priorityId']
        BacklogProperty.check_parameter(input_request_params, required_key)
        return self.common('POST',
                           'issues',
                           request_params=input_request_params)

    def update_issue(self, issueIdOrKey, input_request_params={}):
        ''' Update issue '''
        return self.common('PATCH',
                           'issues/{issueIdOrKey}',
                           url_params={'issueIdOrKey': issueIdOrKey},
                           request_params=input_request_params)

    def get_issue_attachments(self, issueIdOrKey):
        ''' Get issue attachments '''
        return self.common('GET',
                           'issues/{issueIdOrKey}/attachments',
                           url_params={'issueIdOrKey': issueIdOrKey})

    def delete_issue_attachments(self, issueIdOrKey, attachmentId):
        ''' Delete issue attachments'''
        return self.common('DELETE',
                           'issues/{issueIdOrKey}/attachments/{attachmentId}',
                           url_params={'issueIdOrKey': issueIdOrKey,
                                       'attachmentId': attachmentId})

    # Addmin User functions
    def get_space_capacity(self):
        ''' Get space capacity '''
        return self.common('GET', 'space/diskUsage')

    def get_users(self):
        ''' Get user list '''
        return self.common('GET', 'users')

    def add_user(self, input_request_params):
        ''' Add user '''
        required_key = ['userId', 'password', 'name',
                        'mailAddress', 'roleType']
        BacklogProperty.check_parameter(input_request_params, required_key)
        return self.common('POST', 'users',
                           request_params=input_request_params)

    def delete_user(self, userId):
        ''' Delete user'''
        return self.common('DELETE',
                           'users/{userId}',
                           url_params={'userId': userId})

    def add_project(self, input_request_params):
        ''' Add project '''
        required_key = ['name', 'key', 'chartEnabled',
                        'projectLeaderCanEditProjectLeader',
                        'subtaskingEnabled', 'textFormattingRule']
        BacklogProperty.check_parameter(input_request_params, required_key)
        return self.common('POST', 'projects',
                           request_params=input_request_params)

    def delete_project(self, projectIdOrKey):
        ''' Delete project '''
        return self.common('DELETE',
                           'projects/{projectIdOrKey}',
                           url_params={'projectIdOrKey': projectIdOrKey})

    def add_project_user(self, projectIdOrKey, input_request_params):
        ''' Add project user '''
        required_key = ['userId']
        BacklogProperty.check_parameter(input_request_params, required_key)
        return self.common('POST',
                           'projects/{projectIdOrKey}/users',
                           url_params={'projectIdOrKey': projectIdOrKey},
                           request_params=input_request_params)

    def delete_project_user(self, projectIdOrKey, input_request_params):
        ''' Delete project user '''
        required_key = ['userId']
        BacklogProperty.check_parameter(input_request_params, required_key)
        return self.common('DELETE',
                           'projects/{projectIdOrKey}/users',
                           url_params={'projectIdOrKey': projectIdOrKey},
                           request_params=input_request_params)

    def add_project_admin(self, projectIdOrKey, input_request_params):
        ''' Add project admin user '''
        required_key = ['userId']
        BacklogProperty.check_parameter(input_request_params, required_key)
        return self.common('POST',
                           'projects/{projectIdOrKey}/administrators',
                           url_params={'projectIdOrKey': projectIdOrKey},
                           request_params=input_request_params)

    def delete_project_admin(self, projectIdOrKey, input_request_params):
        ''' Delete project admin user '''
        required_key = ['userId']
        BacklogProperty.check_parameter(input_request_params, required_key)
        return self.common('DELETE',
                           'projects/{projectIdOrKey}/administrators',
                           url_params={'projectIdOrKey': projectIdOrKey},
                           request_params=input_request_params)

    def delete_issue(self, issueIdOrKey):
        ''' Delete issue '''
        return self.common('DELETE',
                           'issues/{issueIdOrKey}',
                           url_params={'issueIdOrKey': issueIdOrKey})

    # -------------------------------------------------------
    # Adding function
    # -------------------------------------------------------

    def get_all_issues(self, keys, input_query_params={}):
        ''' Get All issues id and name '''
        input_query_params['offset'] = 0
        while True:
            issues = self.get_issues(input_query_params)
            if len(issues) == 0:
                break
            input_query_params['offset'] += len(issues)
            for issue in issues:
                yield issue
