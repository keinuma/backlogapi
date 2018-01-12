# Backlog課題削除
## 開発環境
* python3.6

## ライブラリ
* pandas

## 使用方法
### プロジェクトコードの入手
'''
python kei_delete_issues.py project
'''

### 課題の検索
* 同ディレクトリにissue_list.csvを作成(課題添付ファイルの場合はissue→attachment)
* issue_list.csvにprojectId,updatedUntil（プロジェクトID、課題更新日）を入力
'''
python kei_delete_issues.py issue_list.csv
'''

### 課題の削除
* 課題の検索で作成したcsvファイルを引数に入れる
* csvを確認して、削除して欲しくない時はレコードを削除する
'''
python kei_delete_issues.py delete_issues_list.csv
'''
