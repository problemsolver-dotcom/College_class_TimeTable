from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

TIMETABLE_DATA = {
    'Monday': [
        {"time": "9:00 AM – 10:00 AM", "subject": "Signals and Systems", "type": "Lecture", "location": "CS7"},
        {"time": "10:00 AM – 11:00 AM", "subject": "Environmental Studies", "type": "Lecture", "location": "LT3"},
        {"time": "11:00 AM – 12:00 PM", "subject": "Signals and Systems", "type": "Tutorial", "location": "F10"},
        {"time": "12:00 PM – 1:00 PM", "subject": "Economics", "type": "Lecture", "location": "CS8"},
        {"time": "2:00 PM – 3:00 PM", "subject": "Digital Circuit Design", "type": "Lecture", "location": "FF2"},
        {"time": "3:00 PM – 4:00 PM", "subject": "Probability and Random Processes", "type": "Tutorial", "location": "TS13"}
    ],
    'Tuesday': [
        {"time": "9:00 AM – 10:00 AM", "subject": "Signals and Systems", "type": "Lecture", "location": "F6"},
        {"time": "10:00 AM – 11:00 AM", "subject": "Electronic Devices and Circuits", "type": "Lecture", "location": "G1"},
        {"time": "11:00 AM – 12:00 PM", "subject": "Probability and Random Processes", "type": "Lecture", "location": "CS8"},
        {"time": "2:00 PM – 3:00 PM", "subject": "Digital Circuit Design", "type": "Tutorial", "location": "F7"},
        {"time": "3:00 PM – 5:00 PM", "subject": "Electronic Devices and Circuits", "type": "Lab", "location": "ADC"}
    ],
    'Wednesday': [
        {"time": "11:00 AM – 1:00 PM", "subject": "Signals and Systems", "type": "Lab", "location": "MODLAB"},
        {"time": "2:00 PM – 3:00 PM", "subject": "Electronic Devices and Circuits", "type": "Lecture", "location": "G3"}
    ],
    'Thursday': [
        {"time": "9:00 AM – 10:00 AM", "subject": "Economics", "type": "Tutorial", "location": "TS12"},
        {"time": "10:00 AM – 11:00 AM", "subject": "Probability and Random Processes", "type": "Lecture", "location": "FF8"},
        {"time": "11:00 AM – 12:00 PM", "subject": "Environmental Studies", "type": "Lecture", "location": "CR425"},
        {"time": "12:00 PM – 1:00 PM", "subject": "Electronic Devices and Circuits", "type": "Lecture", "location": "G3"}
    ],
    'Friday': [
        {"time": "9:00 AM – 10:00 AM", "subject": "Probability and Random Processes", "type": "Lecture", "location": "FF8"},
        {"time": "10:00 AM – 11:00 AM", "subject": "Economics", "type": "Lecture", "location": "FF7"},
        {"time": "11:00 AM – 12:00 PM", "subject": "Digital Circuit Design", "type": "Lecture", "location": "CS6"},
        {"time": "12:00 PM – 1:00 PM", "subject": "Environmental Studies", "type": "Lecture", "location": "G6"},
        {"time": "3:00 PM – 4:00 PM", "subject": "Signals and Systems", "type": "Lecture", "location": "FF7"},
        {"time": "4:00 PM – 5:00 PM", "subject": "Electronic Devices and Circuits", "type": "Tutorial", "location": "TS13"}
    ],
    'Saturday': [
        {"time": "10:00 AM – 11:00 AM", "subject": "Digital Circuit Design", "type": "Lecture", "location": "G2"},
        {"time": "11:00 AM – 1:00 PM", "subject": "Digital Circuit Design", "type": "Lab", "location": "CML"}
    ],
    'Sunday': []
}


@app.route('/')
def index():
    current_day = datetime.now().strftime('%A')
    return render_template('index.html', current_day=current_day)

@app.route('/api/timetable')
def get_timetable():
    return jsonify(TIMETABLE_DATA)

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
