import json
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class Exam:
    name: str
    student_count: int
    duration: int = 2  # Default 2 hours
    scheduled_time: datetime = None
    room: str = None

class ExamManager:
    @staticmethod
    def add_exam(name, student_count):
        try:
            with open("exams.json", "r") as f:
                exams = json.load(f)
        except FileNotFoundError:
            exams = []
        
        exams.append({"name": name, "student_count": student_count})
        
        with open("exams.json", "w") as f:
            json.dump(exams, f, indent=2)

    @staticmethod
    def normalize_exam_data():
        """Normalize existing exam data to use consistent field names"""
        try:
            with open("exams.json", "r") as f:
                exams = json.load(f)
            
            # Convert "students" to "student_count" if needed
            normalized = []
            for exam in exams:
                if "students" in exam and "student_count" not in exam:
                    exam["student_count"] = exam.pop("students")
                normalized.append(exam)
            
            with open("exams.json", "w") as f:
                json.dump(normalized, f, indent=2)
                
        except FileNotFoundError:
            pass

    @staticmethod
    def load_exams():
        try:
            with open("exams.json") as f:
                exam_data = json.load(f)
                exams = []
                for e in exam_data:
                    # Handle both "students" and "student_count" keys for backward compatibility
                    student_count = e.get("student_count") or e.get("students", 0)
                    exams.append(Exam(name=e["name"], student_count=student_count))
                return exams
        except FileNotFoundError:
            return []
