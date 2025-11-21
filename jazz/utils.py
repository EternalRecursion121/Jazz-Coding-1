import os
import json
import requests
from datetime import datetime

# Simple in-memory cache: {url: (timestamp, data)}
api_cache = {}
CACHE_DURATION = 10  # 10 seconds

def get_github_data(url, token=None):
    now = datetime.now()
    if url in api_cache:
        timestamp, data = api_cache[url]
        if (now - timestamp).total_seconds() < CACHE_DURATION:
            return data

    headers = {'Accept': 'application/vnd.github.v3+json'}
    if token:
        headers['Authorization'] = f'token {token}'
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            api_cache[url] = (now, data)
            return data
    except Exception:
        pass
    
    return None

def get_contributor_stats(repo_owner, repo_name, token=None):
    """Fetches commit counts for all contributors in a repo."""
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contributors"
    data = get_github_data(url, token)
    
    stats = {}
    if data:
        for contributor in data:
            login = contributor.get('login')
            count = contributor.get('contributions', 0)
            if login:
                stats[login.lower()] = count
    return stats

def load_participants():
    try:
        # Assuming participants.json is in the project root
        with open('participants.json', 'r') as f:
            return json.load(f)
    except:
        return []
