from flask import Flask, jsonify
from . import status

app = Flask(__name__)

COUNTERS = {}

def counter_exists(name):
    """Check if counter exists"""
    return name in COUNTERS 

@app.route('/counters/<name>', methods=['POST'])
def create_counter(name):
    """Create a counter"""
    if counter_exists(name):
        return jsonify({"error": f"Counter {name} already exists"}), status.HTTP_409_CONFLICT
    COUNTERS[name] = 0
    return jsonify({name: COUNTERS[name]}), status.HTTP_201_CREATED

def reset_counters():
    """Helper function to reset all counters"""
    global COUNTERS
    for key in COUNTERS:
        COUNTERS[key] = 0

@app.route('/counters/reset', methods=['POST'])
def reset_all_counters():
    """Resets all counters using helper function"""
    reset_counters()
    return jsonify({"message": "All counters reset"}), status.HTTP_200_OK
