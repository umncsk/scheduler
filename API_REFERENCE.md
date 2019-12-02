## API
Use your ToyoNet-Ace id and password.

### URLs
#### `localhost:8000/admin`

#### GET `localhost:8000/api/v1/`
all users list
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "user_name": "<user_name>",
            "user_pswd": "encrypted user password",
            "student_id": "<student_id>",
            "student_pswd": "encrypted toyo password"
        },
        ...
    ]
}
```
#### POST `localhost:8000/api/v1/`
user registration
```json
{
    "user_name": [
        "この項目は必須です。"
    ],
    "user_pswd": [
        "この項目は必須です。"
    ],
    "student_id": [
        "この項目は必須です。"
    ],
    "student_pswd": [
        "この項目は必須です。"
    ]
}
```
#### `localhost:8000/users`
#### `localhost:8000/user/<pk>`

## access the data
test stage
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
