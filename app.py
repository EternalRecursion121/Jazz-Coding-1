import os
from flask import Flask, render_template, request, redirect, url_for
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

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<Message {self.name}>'

# Initialize database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    messages = Message.query.order_by(Message.created_at.desc()).limit(10).all()
    return render_template('index.html', name='World', messages=messages)

@app.route('/hello/<name>')
def hello(name):
    messages = Message.query.order_by(Message.created_at.desc()).limit(10).all()
    return render_template('index.html', name=name, messages=messages)

@app.route('/add_message', methods=['POST'])
def add_message():
    name = request.form.get('name', 'Anonymous')
    content = request.form.get('content', '')
    if content:
        message = Message(name=name, content=content)
        db.session.add(message)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Use PORT environment variable if available (Railway provides this)
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)

