from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json, os, hashlib

app = Flask(__name__)
app.secret_key = 'fromage_secret_key_2024'

USERS_FILE = 'users.json'

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE) as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f)

def hash_password(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

def load_cheeses():
    with open('static/cheeses.json') as f:
        return json.load(f)

@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('explore'))
    return redirect(url_for('auth'))

@app.route('/auth')
def auth():
    return render_template('auth.html')

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username', '').strip()
    email = data.get('email', '').strip()
    password = data.get('password', '').strip()
    if not username or not email or not password:
        return jsonify({'error': 'Please fill all fields'}), 400
    users = load_users()
    if username in users:
        return jsonify({'error': 'Username already taken!'}), 400
    for u in users.values():
        if isinstance(u, dict) and u.get('email') == email:
            return jsonify({'error': 'Email already registered!'}), 400
    users[username] = {'password': hash_password(password), 'email': email}
    save_users(users)
    session['user'] = username
    return jsonify({'success': True})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username', '').strip()
    password = data.get('password', '').strip()
    users = load_users()
    if username not in users:
        return jsonify({'error': 'Invalid username or password!'}), 401
    user_data = users[username]
    stored_hash = user_data['password'] if isinstance(user_data, dict) else user_data
    if stored_hash != hash_password(password):
        return jsonify({'error': 'Invalid username or password!'}), 401
    session['user'] = username
    return jsonify({'success': True})

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('auth'))

@app.route('/explore')
def explore():
    if 'user' not in session:
        return redirect(url_for('auth'))
    return render_template('explore.html', user=session['user'])

@app.route('/api/cheeses/all')
def api_cheeses_all():
    return jsonify(load_cheeses())

@app.route('/api/cheeses')
def api_cheeses():
    cheeses = load_cheeses()
    flavors = request.args.getlist('flavor')
    textures = request.args.getlist('texture')
    milk = request.args.getlist('milk')
    vegetarian = request.args.get('vegetarian', '')

    # If no filters at all, return empty — user must select something
    if not flavors and not textures and not milk and not vegetarian:
        return jsonify([])

    results = []
    for c in cheeses:
        if flavors:
            cheese_flavors = [f.strip().lower() for f in c['flavor'].split(',')]
            if not any(fl.lower() in cheese_flavors for fl in flavors):
                continue
        if textures:
            cheese_textures = [t.strip().lower() for t in c['texture'].split(',')]
            if not any(tx.lower() in cheese_textures for tx in textures):
                continue
        if milk:
            cheese_milks = [m.strip().lower() for m in c['milk'].split(',')]
            if not any(mk.lower() in cheese_milks for mk in milk):
                continue
        if vegetarian == 'true' and c['vegetarian'] != 'TRUE':
            continue
        results.append(c)

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, port=5000)