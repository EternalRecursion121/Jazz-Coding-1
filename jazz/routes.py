import os
from datetime import datetime
from flask import Blueprint, render_template
from jazz.utils import get_github_data, load_participants

bp = Blueprint('jazz', __name__, template_folder='templates')

@bp.route('/jazz')
def dashboard():
    participants = load_participants()
    github_token = os.environ.get('GITHUB_TOKEN')
    
    stats = []
    now = datetime.now()
    
    # Optimization: Cache contributor lists per repo identifier to avoid refetching
    # Key: "owner/repo", Value: {username: count}
    repo_stats_cache = {}

    for p in participants:
        username = p['username']
        repo_field = p.get('repo', '')
        
        # Determine Repo Owner/Name
        if '/' in repo_field:
            owner, repo_name = repo_field.split('/', 1)
        else:
            owner, repo_name = username, repo_field
            
        repo_full_name = f"{owner}/{repo_name}"
        
        start_date = datetime.strptime(p['start_date'], '%Y-%m-%d')
        max_inactivity_days = len(participants)
        
        # 1. Get Last Commit (Liveness)
        # We assume they are committing to the repo specified
        url_commits = f"https://api.github.com/repos/{owner}/{repo_name}/commits?author={username}&per_page=1"
        commit_data = get_github_data(url_commits, github_token)
        
        last_commit_date = start_date
        days_since_commit = (now - start_date).days
        
        if commit_data and len(commit_data) > 0:
            commit_str = commit_data[0]['commit']['author']['date']
            last_commit_date = datetime.strptime(commit_str, "%Y-%m-%dT%H:%M:%SZ")
            days_since_commit = (now - last_commit_date).days
            
        # 2. Get Total Commits (Race Progress)
        # We use the contributors endpoint which gives counts
        if repo_full_name not in repo_stats_cache:
            url_contrib = f"https://api.github.com/repos/{owner}/{repo_name}/contributors"
            contrib_data = get_github_data(url_contrib, github_token)
            
            # Map login -> contributions
            counts = {}
            if contrib_data:
                for c in contrib_data:
                    if 'login' in c:
                        counts[c['login'].lower()] = c.get('contributions', 0)
            repo_stats_cache[repo_full_name] = counts
            
        total_commits = repo_stats_cache[repo_full_name].get(username.lower(), 0)

        # Determine status
        is_dead = days_since_commit > max_inactivity_days
        days_left = max(0, max_inactivity_days - days_since_commit)
        
        stats.append({
            'username': username,
            'name': p.get('name', username),
            'status': 'DEAD' if is_dead else 'ALIVE',
            'days_left': days_left,
            'last_commit': last_commit_date.strftime('%Y-%m-%d'),
            'total_commits': total_commits,
            'repo': repo_name
        })
        
    # Sort by total commits (race leader)
    stats.sort(key=lambda x: x['total_commits'], reverse=True)
        
    return render_template('dashboard.html', stats=stats, max_days=len(participants))
