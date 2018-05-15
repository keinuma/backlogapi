# Delete some attachment in issue
## Other library
* pandas

## How to use
### Get project information
```
python kei_delete_issues.py project
```

### Search issue with attachment
- Make issues_list.csv (ex. input/issues_list.csv)
- Write issue query parameter in issues_list.csv .
- Parameter is projectId, updatedUntil
```
python kei_delete_issues.py issue_list.csv
```

### Delete attachment
- Delete attachment is:
```
python kei_delete_issues.py delete_issues_list.csv
```
