from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from void.models import Scream, db

bp = Blueprint('void', __name__, template_folder='templates')

@bp.route('/')
def index():
    return render_template('scream.html')

@bp.route('/void')
def enter_void():
    return render_template('void.html')

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
