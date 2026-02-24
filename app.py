"""Coordination Drill Live E2E R03 - Minimal Flask App with Drill Feature"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Simple drill state
drill_state = {
    "counter": 0,
    "history": []
}

@app.route('/')
def index():
    return jsonify({"status": "ok", "service": "coordination-drill-live-e2e-r03"})

@app.route('/health')
def health():
    return jsonify({"health": "healthy"})

@app.route('/drill', methods=['GET', 'POST'])
def drill():
    """Small drill feature: increment counter and record history"""
    if request.method == 'POST':
        drill_state['counter'] += 1
        drill_state['history'].append(f"drill-{drill_state['counter']}")
        return jsonify({
            "counter": drill_state['counter'],
            "action": "incremented"
        })
    else:
        return jsonify({
            "counter": drill_state['counter'],
            "history": drill_state['history'][-5:]
        })

@app.route('/drill/reset', methods=['POST'])
def drill_reset():
    """Reset drill state"""
    drill_state['counter'] = 0
    drill_state['history'] = []
    return jsonify({"status": "reset", "counter": 0})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)