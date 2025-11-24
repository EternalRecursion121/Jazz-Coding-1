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

## Face Detection System

Real-time face tracking overlay using MediaPipe Face Detection.

### Implementation
- **Canvas**: `#face-canvas` overlay at `z-index: 50`
- **Video**: Hidden camera feed for MediaPipe processing
- **Model**: MediaPipe 'short' range, 0.5 confidence threshold

### Rendering
- **Bounding boxes**: `strokeStyle: rgba(255,255,255,0.8)`, `lineWidth: 2`
- **Landmarks**: `fillStyle: rgba(255,255,255,0.9)`, 5px radius circles
- **Coordinates**: MediaPipe normalized (0.0-1.0) × canvas dimensions
- **Mirroring**: X-coordinates flipped for natural movement matching

### Stabilization
- **Frame averaging**: Rolling 5-frame history for smooth tracking
- **Confidence filtering**: Only updates with >0.7 confidence detections
- **Temporal smoothing**: Averages bounding box and landmark positions

### Debug Controls
- Set `DEBUG_VIDEO = true` to show mirrored camera feed
- Console: `toggleDebugVideo()` helper (requires page reload)

### Revelation API
- `setVoidRevelation(boolean)` - reveals/hides screams clearly
- `getVoidRevelation()` - returns current revelation state

