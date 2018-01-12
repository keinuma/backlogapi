# Backlog API Library
## 開発環境
### Python
* python3.6.1

### ライブラリ
* requests 2.18.4

## How To Use
### 一般ユーザ
'''python


    import backlogapi

    # 初期設定でspace名とapi keyを設定
    client = backlogapi.BacklogProperty(space, apikey)

    # スペース名を取得
    client.get_space()

    # プロジェクトの一覧を取得
    # 発行したAPIユーザーが参加しているプロジェクトのみ取得される
    # オプションとしてクエリパラメーターを設定できる
    client.get_projects(query_params)

    # プロジェクト情報の詳細を取得
    client.get_project_info(projectID)

    # 共有ファイルの一覧の取得
    # 共有ファイルはプロジェクトIDとpathが必要
    client.get_sharefile(projectIdOrKey, path, query_params)

    # 課題一覧の取得
    # 条件をクエリパラメーターに設定することができる
    client.get_issues(projectIdOrKey, {'created': YYYY-MM-DD})

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

'''

### 管理者ユーザ
* 追記予定


### 更新情報
* 2017/09/02 README追記
