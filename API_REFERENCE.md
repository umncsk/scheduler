Here is API reference.
Use your [ToyoNet-ACE](https://www.ace.toyo.ac.jp/ct/home) ID and password.

## Usage
HTTP request              | Description
---                       | ---
`GET /api/users/`         | Get user list.
`POST /api/users/`        | Add new user.
`GET /api/organizations`  | Get organization list.
`POST /api/organizations` | Add new organization.

## Debugging
```console
>>> from app_scheduler.models import User
>>> User
<class 'app_scheduler.models.User'>
>>> User.objects.all()
<QuerySet [<User: s1F101704017>]>
>>> user = User(username='hoge', password='hoge', student_id='s1F1017xxxxx')
>>> user.save()
>>> user
<User: s1F1017xxxxx>
>>> user.username
'hoge'
>>> User.objects.all()
<QuerySet [<User: s1F101704017>, <User: s1F1017xxxxx>]>
>>> sk = User.objects.get(username='sk')
>>> sk.username
'sk'
>>> sk.schedule
'010000000101100001010000001110000110000000000000'
>>> 
```
