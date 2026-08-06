from user import User
from vip_user import VIPUser


def create_user_from_data(item: dict) -> User:
    user_class = VIPUser if item["type"] == "vip" else User

    return user_class(
        item["name"],
        item["money"],
        item["income"]
    )