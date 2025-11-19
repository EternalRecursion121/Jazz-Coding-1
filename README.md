# T H E  V O I D

A digital abyss where messages drift, rot, and fade into obscurity. Built with Flask and PostgreSQL.

## C O N C E P T

The Void is an interactive art piece and anonymous message board.

- **Scream**: Post messages anonymously into the database.
- **Drift**: Messages float aimlessly through the browser window in the visualizer.
- **Rot**: Text corrupts over time using Zalgo glitches. The older the message, the more unreadable it becomes.
- **Insanity**: The longer you stay on the page, the more the screen blurs, shifts hues, and shakes.

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Enter the void:
   - http://localhost:8080/

## Project Structure

```
.
├── app.py              # The Void's backend (Flask + SQLAlchemy)
├── templates/
│   ├── scream.html     # The input interface (Entry)
│   └── void.html       # The visualization interface (The Abyss)
├── requirements.txt    # Dependencies
└── README.md           # You are here
```

## Database Model

**Scream**
- `id`: Integer
- `content`: Text (The scream)
- `created_at`: DateTime (Used to calculate decay)
