from flask import Flask, render_template, jsonify
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# --- Data ---
# This data is now managed by the backend.
TIMETABLE_DATA = {
    'Monday': [
        {"time": "9:00–10:00", "subject": "Signals and System", "type": "Lecture", "location": "CS7"},
        {"time": "10:00–11:00", "subject": "Environmental Studies", "type": "Lecture", "location": "LT3"},
        {"time": "11:00–12:00", "subject": "Signals and System", "type": "Tutorial", "location": "F10"},
        {"time": "12:00–1:00", "subject": "Economics", "type": "Lecture", "location": "CS8"},
        {"time": "2:00–3:00", "subject": "Digital Circuit Design", "type": "Lecture", "location": "FF2"},
        {"time": "3:00–4:00", "subject": "Probability and Random Processes", "type": "Tutorial", "location": "TS13"}
    ],
    'Tuesday': [
        {"time": "9:00–10:00", "subject": "Signals and System", "type": "Lecture", "location": "F6"},
        {"time": "10:00–11:00", "subject": "Electronic Devices and Circuits", "type": "Lecture", "location": "G1"},
        {"time": "11:00–12:00", "subject": "Probability and Random Processes", "type": "Lecture", "location": "CS8"},
        {"time": "2:00–3:00", "subject": "Digital Circuit Design", "type": "Tutorial", "location": "F7"},
        {"time": "3:00–5:00", "subject": "Electronic Devices and Circuits", "type": "Lab", "location": "ADC"}
    ],
    'Wednesday': [
        {"time": "11:00–1:00", "subject": "Signals and Systems", "type": "Lab", "location": "MODLAB"},
        {"time": "2:00–3:00", "subject": "Electronic Devices and Circuits", "type": "Lecture", "location": "G3"}
    ],
    'Thursday': [
        {"time": "9:00–10:00", "subject": "Economics", "type": "Tutorial", "location": "TS12"},
        {"time": "10:00–11:00", "subject": "Probability and Random Processes", "type": "Lecture", "location": "FF8"},
        {"time": "11:00–12:00", "subject": "Environmental Studies", "type": "Lecture", "location": "CR425"},
        {"time": "12:00–1:00", "subject": "Electronic Devices and Circuits", "type": "Lecture", "location": "G3"}
    ],
    'Friday': [
        {"time": "9:00–10:00", "subject": "Probability and Random Processes", "type": "Lecture", "location": "FF8"},
        {"time": "10:00–11:00", "subject": "Economics", "type": "Lecture", "location": "FF7"},
        {"time": "11:00–12:00", "subject": "Digital Circuit Design", "type": "Lecture", "location": "CS6"},
        {"time": "12:00–1:00", "subject": "Environmental Studies", "type": "Lecture", "location": "G6"},
        {"time": "3:00–4:00", "subject": "Signals and System", "type": "Lecture", "location": "FF7"},
        {"time": "4:00–5:00", "subject": "Electronic Devices and Circuits", "type": "Tutorial", "location": "TS13"}
    ],
    'Saturday': [
        {"time": "10:00–11:00", "subject": "Digital Circuit Design", "type": "Lecture", "location": "G2"},
        {"time": "11:00–1:00", "subject": "Digital Circuit Design", "type": "Lab", "location": "CML"}
    ],
    'Sunday': []
}

# --- Routes ---

@app.route('/')
def index():
    """
    Main route to render the timetable interface.
    It passes the current day of the week to the template.
    """
    # The current date is Thursday, July 31, 2025.
    current_day = datetime.now().strftime('%A')
    return render_template('index.html', current_day=current_day)

@app.route('/api/timetable')
def get_timetable():
    """
    API endpoint to provide the entire timetable data as JSON.
    The frontend will fetch data from this endpoint.
    """
    return jsonify(TIMETABLE_DATA)

# --- Error Handlers ---

@app.errorhandler(404)
def not_found_error(error):
    """Handles 404 Not Found errors."""
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handles 500 Internal Server errors."""
    return jsonify({"error": "Internal server error"}), 500

# --- Main Execution ---

if __name__ == '__main__':
    # Runs the app in debug mode, accessible on your local network.
    app.run(debug=True, host='0.0.0.0', port=5000)
