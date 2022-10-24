from .router import TreeItemView, prefix


tree_router = [
    ("GET", prefix, TreeItemView),
]
