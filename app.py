import os
import jinja2
from flask import Flask
from void.models import db

def create_app():
    app = Flask(__name__)

    # Database configuration
    database_url = os.environ.get('DATABASE_URL')
    if database_url and database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)

    app.config['SQLALCHEMY_DATABASE_URI'] = database_url or 'sqlite:///local.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Register Blueprints
    from void.routes import bp as void_bp
    from jazz.routes import bp as jazz_bp

    app.register_blueprint(void_bp)
    app.register_blueprint(jazz_bp)
    
    # Add shared templates to Jinja loader
    # We use ChoiceLoader to look in app templates (default), shared, and blueprint templates
    my_loader = jinja2.ChoiceLoader([
        app.jinja_loader,
        jinja2.FileSystemLoader(['shared/templates']),
    ])
    app.jinja_loader = my_loader

    # Create tables
    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
