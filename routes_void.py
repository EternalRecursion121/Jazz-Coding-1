from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app import db, Scream # We will circular import if we're not careful, but for this simple structure, importing db from app is okay if app initializes it. Actually better to pass db/app or use current_app extensions. 
# Note: In simple flask, importing db from app is common but can cause issues. Ideally db is in extensions.py. 
# For now, I will assume app.py creates db and I'll refactor app.py to expose it properly or keep Scream model there.

bp = Blueprint('void', __name__)

from models import Scream, db # I will move models to a separate file to avoid circular imports

@bp.route('/')
def index():
    return render_template('void/scream.html')

@bp.route('/void')
def enter_void():
    return render_template('void/void.html')

@bp.route('/scream', methods=['POST'])
def scream():
    content = request.form.get('content', '')
    if not content and request.is_json:
        content = request.json.get('content', '')
        
    if content:
        scream = Scream(content=content)
        db.session.add(scream)
        db.session.commit()
        
        if request.is_json:
            return jsonify({'status': 'success', 'scream': scream.to_dict()})
            
    return redirect(url_for('void.index'))

@bp.route('/api/screams')
def get_screams():
    limit = request.args.get('limit', 50, type=int)
    screams = Scream.query.order_by(Scream.created_at.desc()).limit(limit).all()
    return jsonify([s.to_dict() for s in screams])
