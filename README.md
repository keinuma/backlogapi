# Backlog API
Backlog API is client library for using backlog API.
This library provides simple connection to RESTful API by CRUD function.

```python
>>> from backlogapi import BacklogClient

>>> client = BacklogClient(api_key='your_key', space_name='space')
>>> space = client.space.get()
>>> space.id
18812

>>> projects = client.project.all()
>>> project1 = projects[0]

>>> project1.name
project1
    
>>> users_in_project1 = project1.users
>>> users_in_project1
[<User: user1>, <User: user2>]

>>> # get issue in the project and can add parameter
>>> parent_issues_in_project1 = project1.get_issue({'parentChild': 4})
>>> issue1 = parent_issues_in_project1[0]

>>> issue1.due_date
'2018-05-25T12:00:00Z'
```

## Future
* Support all API
* Support OAuth 2.0
and any more

## Requirements
* Python 3.6
* requests 2.18.4


## Installation
```
$ pip intsall backlogapi
```


## License
This software is licensed under the MIT license.
