import sys
from copy import copy
import pandas as pd

from backlogapi import BacklogClient, Issue, IssueAttachment


_GET_ISSUE_QUERY = {
    'projectId[]': 0,
    'count': 100,
    'createdUntil': '2000-01-01',
    'updatedUntil': '2000-01-01',
    'attachment': 'true',
}


def kei_get_project_id(client):
    """
    Get all project and return project id, name
    """
    projects = client.project.all()
    return [(x.id, x.name) for x in projects]


def kei_get_issues(client, query):
    issues = client.issue.filter(query_params=query, upper_limit=True)
    for issue in issues:
        yield issue


def create_issues_report(issue_gene, csv_data_name):
    issues = [(x.id, x.name, x.issue_key, x.created, x.updated, x.parend_issue_id)
              for x in list(copy(issue_gene))]
    issues_frame = pd.DataFrame(issues,
                                columns=['issue_id',
                                         'issue_name',
                                         'issue_key',
                                         'created',
                                         'updated',
                                         'parentIssueId']).fillna(0)
    issues_frame.to_csv(csv_data_name + '.csv', encoding='utf-8', index=False)
    return issues_frame


def kei_delete_issues(client, issues):
    for issue_id in issues['issue_id']:
        try:
            client.issue.delete(issue_id)
        except Exception:
            print('Invalid issue id')
    print('Success')


def kei_delete_attachments(client, attachments):
    for issue_id, attachment_id in zip(attachments['issue_id'], attachments['attachment_id']):
        try:
            Issue(client, issue_id).get_attachments(attachment_id)[0].delete()
        except Exception:
            print('Invalid issue id or attachment id')
    print('Success')


def main(flag, client):
    if flag == 'projects':
        projects = pd.DataFrame(kei_get_project_id(client), columns=['project_id', 'project_name'])
        projects.to_csv('projects-report.csv', index=False)
    elif flag == 'issues_list.csv':
        query_data = pd.read_csv(flag)
        _GET_ISSUE_QUERY['projectId[]'] = query_data['projectId']
        _GET_ISSUE_QUERY['createdUntil'] = query_data['updatedUntil']
        _GET_ISSUE_QUERY['updatedUntil'] = query_data['updatedUntil']
        issue_gene = kei_get_issues(client, _GET_ISSUE_QUERY)
        issues_frames = create_issues_report(issue_gene, 'delete_issues_list')
        print('Success.', issues_frames)
    else:
        print('Flag value is invalid. Please input correct args.')
        sys.exit(1)


def main_deletes(client, flag):
    delete_data_frame = pd.read_csv(flag, encoding='utf-8')
    if flag == 'delete_issues_list.csv':
        kei_delete_issues(client, delete_data_frame)
    elif flag == 'delete_attachments_list.csv':
        kei_delete_attachments(client, delete_data_frame)


if __name__ == '__main__':
    flag_ = sys.argv[1]
    user_client = BacklogClient(api_key='your_api_key', space_name='your_space_name')
    if flag_ == 'delete_issues_list.csv' or flag_ == 'delete_attachments_list.csv':
        main_deletes(user_client, flag_)
    main(flag_, user_client)
