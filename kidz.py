users = [
    {"name": "Stan", "kids": ["John", "Mary"]},
    {"name": "Donald", "kids": ["James"]},
    {"name": "Lily", "kids": []},
    {"name": "Julian", "kids": []},
]


def has_kids(users) -> bool:
    for user in users:
        if user["kids"]:
            print(f"{user['name']} has kids: {', '.join(user['kids'])}")
        else:
            print(f"{user['name']} has no kids.")

has_kids(users)