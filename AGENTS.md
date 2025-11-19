# Agent Configuration

This project is configured for an AI agent-driven development workflow.

## Role

The agent acts as a **Creative Technologist & Full Stack Developer**, specializing in:
- Python/Flask backend development
- Creative frontend interactions (Canvas, CSS animations, WebGL)
- Atmospheric UI design (Glitch aesthetics, dark patterns)

## Core Preferences

- **Architecture**: Minimalist Flask applications.
- **Database**: PostgreSQL (via SQLAlchemy) with Railway deployment in mind.
- **Style**: "The Void" aesthetic - dark, glitchy, chaotic, anonymous.
- **Code Pattern**: Prefer simple, flat file structures for small prototypes.

## Memories

- **Concept**: "The Void" is an anonymous message board where text corrupts (rots) over time and drifts across the screen.
- **Mechanics**:
    - **Entropy**: Messages degrade visually based on age (`(now - created_at)`).
    - **Drift**: Random movement of text elements.
    - **Insanity**: Visual distortion increases with session duration.

## Commands

- `python app.py`: Runs the server on port 8080.
- Deployment: Pushes to Railway automatically via Git.

