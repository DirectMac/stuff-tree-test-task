from .router import (
    UserCollectionView,
    UserItemView,
    prefix
)

user_router = [
    ("GET", prefix, UserCollectionView),
    ("POST", prefix, UserCollectionView),
    ("GET", prefix + "/{id}", UserItemView),
    ("PUT", prefix + "/{id}", UserItemView),
    ("DELETE", prefix + "/{id}", UserItemView)
]
