# T H E  V O I D  &  J A Z Z

An interactive art piece and gamified coding tracker.

## Modules

This project is split into two distinct experiences:

1.  **[The Void](docs/void.md)**: An anonymous abyss where messages rot and drift.
2.  **[Jazz Coding](docs/jazz.md)**: A high-stakes commit tracker for you and your friends.

## Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Jazz (Optional)**:
   - Edit `participants.json` to add your friends.
   - Set `GITHUB_TOKEN` env var if you have many participants.

3. **Run**:
   ```bash
   python app.py
   ```

4. **Explore**:
   - Void: http://localhost:8080/
   - Jazz: http://localhost:8080/jazz

## Project Structure

```
.
├── app.py              # Application Entry Point
├── models.py           # Database Models
├── participants.json   # Jazz Config
├── void/               # The Void Module
│   └── routes.py
├── jazz/               # Jazz Tracker Module
│   └── routes.py
├── templates/          # HTML Templates
│   ├── shared/         # Base layout
│   ├── void/           # Void pages
│   └── jazz/           # Jazz pages
├── static/             # CSS/JS
└── docs/               # Documentation
```

## Theme
See [Theme Documentation](docs/theme.md) for styling details.
