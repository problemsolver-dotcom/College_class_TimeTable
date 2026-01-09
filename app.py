from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

TIMETABLE_DATA = {
    'Monday': [
        {
            "time": "10:00AM – 10:50AM",
            "subject": "Principles of Management",
            "type": "Lecture",
            "location": "G-3"
        },
        {
            "time": "11:00AM – 11:50AM",
            "subject": "Theory and Applications of Linear Algebra",
            "type": "Lecture",
            "location": "G-9"
        },
        {
            "time": "3:00PM – 3:50PM",
            "subject": "Analog and Digital Communication",
            "type": "Lecture",
            "location": "FF-6"
        },
        {
            "time": "4:00PM – 4:50PM",
            "subject": "Telecommunication Networks",
            "type": "Lecture",
            "location": "FF-5"
        }
    ],

    'Tuesday': [
        {
            "time": "10:00AM – 10:50AM",
            "subject": "Theory and Applications of Linear Algebra",
            "type": "Lecture",
            "location": "FF-7"
        },
        {
            "time": "11:00AM – 12:50PM",
            "subject": "Introduction to Artificial Intelligence With Python",
            "type": "Lab",
            "location": "CADLAB"
        },
        {
            "time": "2:00PM – 2:50PM",
            "subject": "Principles of Management",
            "type": "Lecture",
            "location": "FF-5"
        },
        {
            "time": "3:00PM – 3:50PM",
            "subject": "Telecommunication Networks",
            "type": "Lecture",
            "location": "FF-7"
        },
        {
            "time": "4:00PM – 4:50PM",
            "subject": "Analog and Digital Communication",
            "type": "Tutorial",
            "location": "TS-16"
        }
    ],

    'Wednesday': [
        {
            "time": "10:00AM – 10:50AM",
            "subject": "Theory and Applications of Linear Algebra",
            "type": "Lecture",
            "location": "G-7"
        },
        {
            "time": "11:00AM – 12:50PM",
            "subject": "Digital Signal Processing",
            "type": "Lab",
            "location": "MODLAB"
        },
        {
            "time": "2:00PM – 2:50PM",
            "subject": "Principles of Management",
            "type": "Tutorial",
            "location": "FF-7"
        },
        {
            "time": "3:00PM – 3:50PM",
            "subject": "Digital Signal Processing",
            "type": "Lecture",
            "location": "FF-6"
        },
        {
            "time": "4:00PM – 4:50PM",
            "subject": "Introduction to Artificial Intelligence With Python",
            "type": "Lecture",
            "location": "CADLAB"
        }
    ],

    'Thursday': [
        {
            "time": "9:00AM – 9:50AM",
            "subject": "Telecommunication Networks",
            "type": "Lecture",
            "location": "G-6"
        },
        {
            "time": "10:00AM – 10:50AM",
            "subject": "Analog and Digital Communication",
            "type": "Lecture",
            "location": "FF-7"
        },
        {
            "time": "11:00AM – 11:50AM",
            "subject": "Digital Signal Processing",
            "type": "Lecture",
            "location": "G-3"
        },
        {
            "time": "12:00PM – 12:50PM",
            "subject": "Theory and Applications of Linear Algebra",
            "type": "Tutorial",
            "location": "TS-13"
        },
        {
            "time": "3:00PM – 4:50PM",
            "subject": "Applied Mathematical Computational Lab",
            "type": "Lab",
            "location": "MODLAB"
        }
    ],

    'Friday': [
        {
            "time": "10:00AM – 10:50AM",
            "subject": "Analog and Digital Communication",
            "type": "Lecture",
            "location": "FF-6"
        },
        {
            "time": "11:00AM – 11:50AM",
            "subject": "Digital Signal Processing",
            "type": "Lecture",
            "location": "G-9"
        }
    ],

    'Saturday': [
        {
            "time": "9:00AM – 9:50AM",
            "subject": "Digital Signal Processing",
            "type": "Tutorial",
            "location": "TS-16"
        },
        {
            "time": "10:00AM – 11:50AM",
            "subject": "Telecommunication Networks Lab",
            "type": "Lab",
            "location": "ACL"
        }
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
