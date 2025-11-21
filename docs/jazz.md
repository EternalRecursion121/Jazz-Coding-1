# Jazz Coding Tracker

A gamified commit tracker enforcing the "Commit or Die" rule.

## Architecture

- **Blueprint**: `jazz/routes.py`
- **Templates**: `templates/jazz/`
- **Config**: `participants.json` (root directory)

## Configuration

Edit `participants.json` to add friends:

```json
[
    {
        "username": "github_user",
        "repo": "repo_name",
        "start_date": "YYYY-MM-DD"
    }
]
```

### Environment Variables
- `GITHUB_TOKEN`: (Optional) GitHub Personal Access Token. Highly recommended to avoid rate limits.

## Rules

1. **The Game**: Everyone commits to their own repo (or shared).
2. **The Limit**: You must commit at least once every `N` days, where `N` is the number of participants.
3. **The Consequence**: If you fail, you are marked as **DEAD** on the dashboard.

## Routes

### `/jazz` (GET)
The dashboard.
- Fetches commit history for all participants.
- Calculates "Days Left" until death.
- Displays a racecar-style progress bar.
- Dead participants get a glitchy "RIP" status.

