def filter_posts_by_user(posts, user_id):
    """Filter posts by a specific user ID."""
    return [post for post in posts if post["userId"] == user_id]

def sort_posts(posts, key="title", reverse=False):
    """Sort posts by a given key."""
    try:
        return sorted(posts, key=lambda x: x.get(key, ""), reverse=reverse)
    except Exception as e:
        print(f"Sorting error: {e}")
        return posts

def aggregate_posts(posts):
    """Return aggregated stats about posts."""
    if not posts:
        return {"total": 0, "by_user": {}}

    by_user = {}
    for post in posts:
        uid = post["userId"]
        by_user[uid] = by_user.get(uid, 0) + 1

    return {
        "total": len(posts),
        "by_user": by_user
    }
