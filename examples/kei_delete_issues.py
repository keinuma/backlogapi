import sys
import pandas as pd
from backlogapi import BacklogProperty


__GET_ISSUE_QUERY = {
    'projectId[]': 0,
    'count': 100,
    'createdUntil': '2000-01-01',
    'updatedUntil': '2000-01-01'
}


def defin_client(space, api_key):
    return BacklogProperty(space, api_key)


def kei_get_project_id(client):
    projects = client.get_projects()
    return [(x['id'], x['name']) for x in projects]


def kei_get_issues(client, query):
    issue_ids = list(client.get_all_issues(['id',
                                            'summary',
                                            'issueKey',
                                            'created',
                                            'updated',
                                            'parentIssueId'], query))
    yield issue_ids


def create_issues_report(issues, csv_data_name):
    issues_frame = pd.DataFrame(issues,
                                columns=['issue_id',
                                         'issue_name',
                                         'issue_key',
                                         'created',
                                         'updated',
                                         'parentIssueId']).fillna(0)
    issues_frame.to_csv(csv_data_name + '.csv', encoding='utf-8', index=False)
    return issues_frame


def kei_get_attachments(client, query):
    query['attachment'] = 'true'
    issues_attachments = list(client.get_all_issues(['id',
                                                     'summary',
                                                     'issueKey',
                                                     'created',
                                                     'attachments'
                                                     ], query))
    for issue_attachment in issues_attachments:
        for attachment in issue_attachment['attachments']:
            yield [issue_attachment['id'],
                   issue_attachment['summary'],
                   issue_attachment['issueKey'],
                   issue_attachment['created'],
                   attachment['id'],
                   attachment['name'],
                   attachment['size']]


def create_attachments_report(attachments, csv_data_name):
    attachments_frame = pd.DataFrame(attachments,
                                     columns=['issue_id',
                                              'issue_name',
                                              'issue_key',
                                              'created',
                                              'attachment_id',
                                              'attachment_name',
                                              'filesize'],
                                     ).fillna(0)
    attachments_frame.to_csv(csv_data_name + '.csv', encoding='utf-8', index=False)
    return attachments_frame


def kei_delete_issues(client, issues):
    for issue_id in issues['issue_id']:
        try:
            client.delete_issue(issue_id)
        except Exception:
            print('Invaild issue id')
    print('Success')


def kei_delete_attachments(client, attachments):
    for issue_id, attachment_id in zip(attachments['issue_id'], attachments['attachment_id']):
        try:
            client.delete_issue_attachments
        except Exception:
            print('Invaild issue id or attachment id')
    print('Success')


def main(flug, client):
    if flug == 'project':
        projects = pd.DataFrame(kei_get_project_id(client), columns=['project id', 'project name'])
        projects.to_csv('projects-report.csv', encoding='cp932', index=False)
    elif flug == 'issues_list.csv':
        userData = pd.read_csv(flug, encoding='cp932')
        __GET_ISSUE_QUERY['projectId[]'] = userData['projectId']
        __GET_ISSUE_QUERY['createdUntil'] = userData['updatedUntil']
        __GET_ISSUE_QUERY['updatedUntil'] = userData['updatedUntil']
        issues = list(kei_get_issues(client, __GET_ISSUE_QUERY))
        issues_frames = create_issues_report(issues, 'delete_issues_list')
        print('Success.', issues_frames)
    elif flug == 'attachments_list.csv':
        userData = pd.read_csv(flug, encoding='cp932')
        __GET_ISSUE_QUERY['projectId[]'] = userData['projectId']
        __GET_ISSUE_QUERY['createdUntil'] = userData['updatedUntil']
        __GET_ISSUE_QUERY['updatedUntil'] = userData['updatedUntil']
        attachments = list(kei_get_attachments(client, __GET_ISSUE_QUERY))
        attachments_frames = create_attachments_report(attachments, 'delete_attachments_list')
        print('Success.', attachments_frames)
    else:
        print('Flug value is invaild. Plese input correct args.')
        exit()


def main_deletes(client, flug):
    delete_data_frame = pd.read_csv(flug, encoding='utf-8')
    if flug == 'delete_issues_list.csv':
        kei_delete_issues(client, delete_data_frame)
    elif flug == 'delete_attachments_list.csv':
        kei_delete_attachments(client, delete_data_frame)


if __name__ == '__main__':
    flug = sys.argv[2]
    apikey = sys.argv[1]
    spacename = 'kei-net'
    user_client = defin_client(spacename, apikey)
    if flug == 'delete_issues_list.csv' or flug == 'delete_attachments_list.csv':
        main_deletes(user_client, flug)
    main(flug, user_client)
