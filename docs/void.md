# The Void Module

The Void is an anonymous message board and visualization engine.

## Architecture

- **Blueprint**: `void/routes.py`
- **Templates**: `templates/void/`
- **Models**: `Scream` (defined in `models.py`)

## Routes

### `/` (GET)
The entry point. Renders `templates/void/scream.html`.
- Minimalist input form.
- "Enter Void" button triggers warp animation.

### `/void` (GET)
The visualization. Renders `templates/void/void.html`.
- Fetches screams via API.
- Renders drifting text with "rot" (Zalgo glitch) effect based on age.
- "Wake Up" button triggers whiteout animation to exit.

### `/scream` (POST)
Accepts form data or JSON.
- Saves new `Scream` to database.
- Returns JSON if requested, or redirects to index.

### `/api/screams` (GET)
Returns recent screams in JSON format.
- Used by the visualization JS to fetch data.

