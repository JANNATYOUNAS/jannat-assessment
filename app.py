from flask import Flask, render_template, request, jsonify
from api import fetch_posts
from logic import filter_posts_by_user, sort_posts, aggregate_posts
from storage import save_data, load_data

app = Flask(__name__)

@app.route("/")
def index():
    """Main dashboard — load from storage, apply filters."""
    posts = load_data()

    # If nothing stored yet, fetch automatically
    if not posts:
        posts = fetch_posts()
        save_data(posts)

    # Get query parameters
    user_id = request.args.get("user_id", type=int)
    sort_by = request.args.get("sort_by", "title")
    order = request.args.get("order", "asc")

    # Apply filter
    if user_id:
        posts = filter_posts_by_user(posts, user_id)

    # Apply sort
    posts = sort_posts(posts, key=sort_by, reverse=(order == "desc"))

    # Aggregate stats (always on full data)
    all_posts = load_data()
    stats = aggregate_posts(all_posts)

    return render_template("index.html",
                           posts=posts,
                           stats=stats,
                           user_id=user_id,
                           sort_by=sort_by,
                           order=order)

@app.route("/fetch")
def fetch_and_store():
    """Fetch fresh data from API and save to storage."""
    posts = fetch_posts()
    if not posts:
        return jsonify({"error": "Could not fetch data from API"}), 500
    new_count = save_data(posts)
    return jsonify({"message": f"Done! {new_count} new posts saved.", "total": len(posts)})

@app.route("/api/posts")
def api_posts():
    """Return posts as JSON with optional filters."""
    posts = load_data()
    user_id = request.args.get("user_id", type=int)
    sort_by = request.args.get("sort_by", "id")
    order = request.args.get("order", "asc")

    if user_id:
        posts = filter_posts_by_user(posts, user_id)
    posts = sort_posts(posts, key=sort_by, reverse=(order == "desc"))

    return jsonify(posts)

if __name__ == "__main__":
    app.run(debug=True)