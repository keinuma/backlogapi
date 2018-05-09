# Backlog API Library
## 開発環境
### Python
* python3.6.1

### Requirements
* requests 2.18.4

## Sample
```python
    from backlogapi import BacklogClient

    # 初期設定でspace名とapi keyを設定
    client = BacklogClient(api_key='your_key', space_name='space')

    # スペース情報を取得
    client.space.get()

    # プロジェクトの一覧を取得
    # 発行したAPIユーザーが参加しているプロジェクトのみ取得される
    # オプションとしてクエリパラメーターを設定できる
    projects = client.project.all()
    sample_project = projects[0]

    # プロジェクト情報の詳細を取得
    sample_project.get()
    # or 
    client.project.get(sample_project.id)

    # ユーザーが所属しているプロジェクトの全課題の取得
    client.issue.all()
    
    # 課題条件を選択して取得
    client.issue.filter({'projectIdOrKey': sample_project.id})

    # 課題の追加
    # 入力パラメータに必須項目がある
    client.add_issues({'projectID': XXXXXX, 'summary': 'test', 'issueTypeId': 1,
                        'priorityId': 1}])

    # 課題の更新
    # 課題の追加と同じく必須項目あり
    client.update_issue(issueIdOrKey, {summary: 'XXXX'})

    # 課題添付ファイル一覧の取得
    # 課題のIDさえあれば、一覧の有無を取得できる
    client.get_issue_attachments(issueIdOrKey)

    # 課題添付ファイルの削除
    # 課題のIDと課題添付ファイルのIDを利用して削除する
    client.delete_issue_attachments(issueIdOrKey, attachmentId)

```

## Installation
- The recommended way to install is using pip library:
> $ pip install pybacklog


## Documentation
coming soon

### 管理者ユーザ
* 追記予定
