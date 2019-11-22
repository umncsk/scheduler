## API
Use your ToyoNet-Ace id and password.

### URLs
#### `localhost:8000/admin`

#### GET `localhost:8000/`
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
#### POST `localhost:8000/
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
