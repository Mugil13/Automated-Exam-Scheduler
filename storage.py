import json
import os
from datetime import datetime

def load_data():
    exams = []
    rooms = []
        
    if os.path.exists("exams.json"):
        with open("exams.json") as f:
            exams = json.load(f)
        
    if os.path.exists("rooms.json"):
        with open("rooms.json") as f:
            rooms = json.load(f)
    else:
        rooms = [
            {"name": "A101", "capacity": 100},
            {"name": "B202", "capacity": 50},
            {"name": "C303", "capacity": 30}
        ]
        with open("rooms.json", "w") as f:
            json.dump(rooms, f, indent=2)
                
    return exams, rooms

def save_schedule(schedule):
    # Convert Exam objects to dictionaries for JSON serialization
    schedule_data = []
    for exam in schedule:
        exam_dict = {
            "name": exam.name,
            "student_count": exam.student_count,
            "duration": exam.duration,
            "scheduled_time": exam.scheduled_time.isoformat() if exam.scheduled_time else None,
            "room": exam.room
        }
        schedule_data.append(exam_dict)
    
    with open("schedule.json", "w") as f:
        json.dump(schedule_data, f, indent=2)