import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration - Railway provides DATABASE_URL automatically
database_url = os.environ.get('DATABASE_URL')
if database_url and database_url.startswith('postgres://'):
    # Railway uses postgres:// but SQLAlchemy expects postgresql://
    database_url = database_url.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url or 'sqlite:///local.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Scream(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'created_at': self.created_at.isoformat()
        }

# Initialize database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('scream.html')

@app.route('/void')
def void():
    return render_template('void.html')

@app.route('/scream', methods=['POST'])
def scream():
    content = request.form.get('content', '')
    # Handle JSON requests as well for the asynchronous UI
    if not content and request.is_json:
        content = request.json.get('content', '')
        
    if content:
        scream = Scream(content=content)
        db.session.add(scream)
        db.session.commit()
        
        if request.is_json:
            return jsonify({'status': 'success', 'scream': scream.to_dict()})
            
    return redirect(url_for('index'))

@app.route('/api/screams')
def get_screams():
    # Return recent screams for the void drift effect
    limit = request.args.get('limit', 50, type=int)
    screams = Scream.query.order_by(Scream.created_at.desc()).limit(limit).all()
    return jsonify([s.to_dict() for s in screams])

if __name__ == '__main__':
    # Use PORT environment variable if available (Railway provides this)
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
