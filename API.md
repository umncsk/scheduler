## API
Use your ToyoNet-Ace id and password.

### URLs
#### `localhost:8000/admin`

#### `localhost:8000/`
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

#### `localhost:8000/users`
#### `localhost:8000/user/<pk>`
