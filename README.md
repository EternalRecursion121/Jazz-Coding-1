# Flask Quickstart with PostgreSQL

A minimal Flask application with HTML templating using Jinja2 and PostgreSQL database integration, ready for Railway deployment.

## Quick Start (Local)

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and visit:
   - http://localhost:5000/ - Default greeting with message board
   - http://localhost:5000/hello/YourName - Personalized greeting

## Railway Deployment

### Prerequisites
- Railway account (sign up at https://railway.app)
- Git repository (GitHub, GitLab, or Bitbucket)

### Steps

1. **Create a Railway Project**
   - Go to Railway dashboard
   - Click "New Project"
   - Select "Deploy from GitHub repo" (or your Git provider)
   - Choose this repository

2. **Add PostgreSQL Database**
   - In your Railway project, click "+ New"
   - Select "Database" → "Add PostgreSQL"
   - Railway automatically creates a `DATABASE_URL` environment variable

3. **Configure Flask App**
   - The app automatically detects `DATABASE_URL` from Railway
   - No additional configuration needed!

4. **Deploy**
   - Railway will automatically detect Flask and install dependencies
   - Your app will be live at a Railway-provided URL

### Environment Variables

Railway automatically provides:
- `DATABASE_URL` - PostgreSQL connection string (automatically configured)

The app handles the `postgres://` → `postgresql://` conversion automatically for Railway compatibility.

## Project Structure

```
.
├── app.py              # Main Flask application with PostgreSQL
├── templates/          # HTML templates (Jinja2)
│   └── index.html
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Features

- Flask web framework
- Jinja2 templating (built into Flask)
- PostgreSQL database integration (SQLAlchemy)
- Railway-ready deployment configuration
- Message board example demonstrating database operations
- Automatic database URL handling for Railway

## Database Model

The app includes a simple `Message` model with:
- `id` - Primary key
- `name` - Message author name
- `content` - Message content
- `created_at` - Timestamp

Tables are automatically created on first run.

