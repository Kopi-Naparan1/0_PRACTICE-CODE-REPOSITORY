import random

used_ids = set()


def user_id_generator() -> int:
    while True:
        user_id = random.randint(10_000_000, 99_999_999)
        if user_id not in used_ids:
            used_ids.add(user_id)
            return user_id
