# Theme System

The project uses a shared CSS theme to maintain the "Void/Glitch" aesthetic across all modules.

## Key Files

- **CSS**: `static/css/theme.css`
- **Base Layout**: `templates/shared/layout.html`

## Variables

The theme uses CSS variables for easy customization:

```css
:root {
    --glitch-color-1: #ff0000; /* Red glitch */
    --glitch-color-2: #00ff00; /* Green glitch */
    --glitch-color-3: #0000ff; /* Blue glitch */
    --bg-color: #000;          /* Background */
    --text-color: #ccc;        /* Main text */
    --highlight-color: #fff;   /* Hover/Focus */
}
```

## Standard Elements

### CRT Overlay
The `.crt-overlay` class (in layout) adds scanlines and a flicker animation to the entire viewport.

### Typography
Font is `VT323` (Google Fonts), a retro terminal monospace.

### Animations
- `@keyframes flicker`: Subtle screen flicker.
- `@keyframes shake`: Intense jitter for glitch effects (used on hover).
- `@keyframes warp`: Zoom blur for entering the void.
- `@keyframes whiteout`: Brightness blowout for exiting.

