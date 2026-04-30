import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def fetch_posts():
    """Fetch all posts from the API."""
    try:
        response = requests.get(f"{BASE_URL}/posts", timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("Error: Request timed out.")
        return []
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to API.")
        return []
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

def fetch_users():
    """Fetch all users from the API."""
    try:
        response = requests.get(f"{BASE_URL}/users", timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("Error: Request timed out.")
        return []
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to API.")
        return []
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []