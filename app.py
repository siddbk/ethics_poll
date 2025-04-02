"""
AI Ethics Poll Game - Main Flask Application

This is the main entry point for the application that handles:
- Serving the application routes
- Managing the game state
- Coordinating between modules
"""

from flask import Flask, render_template, request, redirect, url_for, jsonify, session
import os
import json
import time
from models import Scenario, Response, GameState
from utils import generate_qr_code, calculate_results, get_ip_address
from config import APP_CONFIG, SCENARIOS

# In app.py
from functools import wraps
from flask import request, Response

def check_auth(username, password):
    """Check if a username/password combination is valid."""
    # Change these credentials!
    return username == 'siddbk' and password == 'admincontrol'

def authenticate():
    """Sends a 401 response that enables basic auth."""
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Admin Area"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

# Then add this decorator to admin routes:
@app.route('/')
@requires_auth
def index():
    """Main admin control panel for the presenter."""
    ip_address = get_ip_address()
    base_url = f"http://{ip_address}:{app.config['PORT']}"
    return render_template('index.html', 
                           scenarios=game.scenarios, 
                           current_scenario=game.current_scenario,
                           base_url=base_url)

app = Flask(__name__)
app.secret_key = os.urandom(24)  # For session management
#app.config.from_object(APP_CONFIG)
for key, value in APP_CONFIG.items():
    app.config[key] = value

# Initialize game state
game = GameState()

@app.route('/start')
def start_game():
    """Initialize or reset the game."""
    game.reset()
    # Load scenarios from configuration
    for scenario_data in SCENARIOS:
        scenario = Scenario(
            id=scenario_data['id'],
            title=scenario_data['title'],
            description=scenario_data['description'],
            options=scenario_data['options'],
            frameworks=scenario_data['frameworks']
        )
        game.add_scenario(scenario)
    return redirect(url_for('index'))

@app.route('/scenario/<scenario_id>')
def set_current_scenario(scenario_id):
    """Set the current active scenario."""
    game.set_current_scenario(scenario_id)
    return redirect(url_for('index'))

@app.route('/qrcode/<scenario_id>')
def get_qrcode(scenario_id):
    """Generate and return a QR code for the voting page."""
    ip_address = get_ip_address()
    vote_url = f"http://{ip_address}:{app.config['PORT']}/vote/{scenario_id}"
    qr_code_path = generate_qr_code(vote_url, scenario_id)
    return redirect(url_for('static', filename=f'qrcodes/{scenario_id}.png'))

@app.route('/vote/<scenario_id>')
def vote_page(scenario_id):
    """Display the voting page for participants."""
    scenario = game.get_scenario(scenario_id)
    if not scenario:
        return "Scenario not found", 404
    
    # Generate a unique voter ID if not present
    if 'voter_id' not in session:
        session['voter_id'] = f"voter_{int(time.time() * 1000)}"
    
    return render_template('vote.html', 
                           scenario=scenario, 
                           voter_id=session['voter_id'])

@app.route('/submit_vote', methods=['POST'])
def submit_vote():
    """Process a vote submission."""
    data = request.get_json()
    
    if not data or 'scenario_id' not in data or 'choice' not in data or 'voter_id' not in data:
        return jsonify({'status': 'error', 'message': 'Invalid data'}), 400
    
    scenario_id = data['scenario_id']
    choice = data['choice']
    voter_id = data['voter_id']
    
    response = Response(
        voter_id=voter_id,
        scenario_id=scenario_id,
        choice=choice
    )
    
    game.add_response(response)
    
    return jsonify({'status': 'success'})

@app.route('/results/<scenario_id>')
def get_results(scenario_id):
    """Get real-time results for a scenario."""
    scenario = game.get_scenario(scenario_id)
    if not scenario:
        return jsonify({'status': 'error', 'message': 'Scenario not found'}), 404
    
    votes = game.get_responses_for_scenario(scenario_id)
    results = calculate_results(votes, scenario.options)
    
    return jsonify({
        'status': 'success',
        'results': results,
        'total_votes': len(votes),
        'frameworks': scenario.frameworks
    })

@app.route('/display')
def display():
    """Public display view for showing on the main screen."""
    return render_template('display.html', current_scenario=game.current_scenario)

@app.route('/api/current_scenario')
def api_current_scenario():
    """API endpoint to get the current scenario."""
    if not game.current_scenario:
        return jsonify({'status': 'waiting'})
    
    scenario = game.get_scenario(game.current_scenario)
    if not scenario:
        return jsonify({'status': 'error', 'message': 'Scenario not found'}), 404
    
    return jsonify({
        'status': 'active',
        'scenario': scenario.to_dict()
    })

@app.route('/export_results')
def export_results():
    """Export all results as JSON."""
    results = {}
    for scenario in game.scenarios:
        votes = game.get_responses_for_scenario(scenario.id)
        results[scenario.id] = {
            'title': scenario.title,
            'votes': calculate_results(votes, scenario.options),
            'total_votes': len(votes),
            'frameworks': scenario.frameworks
        }
    
    timestamp = int(time.time())
    filename = f"results_{timestamp}.json"
    with open(os.path.join('static', 'exports', filename), 'w') as f:
        json.dump(results, f, indent=2)
    
    return redirect(url_for('static', filename=f'exports/{filename}'))

# For local run on wifi connect
# if __name__ == '__main__':
#     # Ensure directories exist
#     #os.makedirs(os.path.join('static', 'qrcodes'), exist_ok=True)
#     #os.makedirs(os.path.join('static', 'exports'), exist_ok=True)
    
#     base_dir = os.path.dirname(os.path.abspath(__file__))
#     os.makedirs(os.path.join(base_dir, 'static', 'qrcodes'), exist_ok=True)
#     os.makedirs(os.path.join(base_dir, 'static', 'exports'), exist_ok=True)
    
#     # Start the Flask app
#     app.run(
#         host='0.0.0.0', 
#         port=APP_CONFIG['PORT'], 
#         debug=APP_CONFIG['DEBUG'])

if __name__ == '__main__':
    # This will only run when you test locally
    # Ensure directories exist
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(os.path.join(base_dir, 'static', 'qrcodes'), exist_ok=True)
    os.makedirs(os.path.join(base_dir, 'static', 'exports'), exist_ok=True)
    
    # Start the Flask app
    app.run(debug=True)