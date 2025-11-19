# T H E  V O I D

A digital abyss where messages drift, rot, and fade into obscurity. Built with Flask and PostgreSQL.

## C O N C E P T

The Void is an interactive art piece and anonymous message board split into two experiences:

### 1. S C R E A M (The Input)
The entry point. A minimalist interface to scream into the abyss.
- **Anonymous**: No names, no logs, just text.
- **Warp**: Clicking "ENTER THE VOID" triggers a high-velocity visual warp animation to transport you to the visualization.

### 2. T H E  V O I D (The Abyss)
The visualization layer where messages drift and decay.
- **Drift**: Messages float aimlessly through the browser window.
- **Rot**: Text corrupts over time using Zalgo glitches (`h̷e̶l̷l̶o`). The older the message, the more unreadable it becomes.
- **Insanity**: The longer you stay on the page, the more the screen blurs, shifts hues, and shakes.
- **Wake Up**: A "Whiteout" exit animation returns you to reality (the input page).

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
│   ├── scream.html     # Entry page (Input + Warp Animation)
│   └── void.html       # Visualization page (Drift + Rot + Whiteout)
├── requirements.txt    # Dependencies
└── README.md           # You are here
```

## Database Model

**Scream**
- `id`: Integer
- `content`: Text (The scream)
- `created_at`: DateTime (Used to calculate decay intensity)
