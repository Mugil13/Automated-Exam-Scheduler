from tabulate import tabulate
from datetime import datetime
import json

class ScheduleVisualizer:
    @staticmethod
    def display_schedule():
        try:
            with open("schedule.json") as f:
                schedule_data = json.load(f)
                
            if not schedule_data:
                print("No exams scheduled")
                return
                
            table_data = []
            for exam in schedule_data:
                # Handle datetime parsing
                if exam.get("scheduled_time"):
                    if isinstance(exam["scheduled_time"], str):
                        scheduled_time = exam["scheduled_time"]
                    else:
                        scheduled_time = str(exam["scheduled_time"])
                else:
                    scheduled_time = "Not scheduled"
                    
                table_data.append([
                    exam["name"],
                    scheduled_time,
                    exam.get("room", "Not assigned"),
                    exam["student_count"]
                ])
            
            print("\nEXAM SCHEDULE:")
            print(tabulate(
                table_data,
                headers=["Exam", "Time", "Room", "Students"],
                tablefmt="grid"
            ))
            
            ScheduleVisualizer.print_calendar_view(schedule_data)
            
        except FileNotFoundError:
            print("No schedule found. Generate one with 'schedule' command")
        except Exception as e:
            print(f"Error displaying schedule: {e}")

    @staticmethod
    def print_calendar_view(schedule):
        print("\nCALENDAR VIEW:")
        
        # Group exams by date
        scheduled_exams = [e for e in schedule if e.get("scheduled_time")]
        if not scheduled_exams:
            print("No scheduled exams to display")
            return
            
        # Extract dates from scheduled_time
        exam_dates = {}
        for exam in scheduled_exams:
            if isinstance(exam["scheduled_time"], str):
                date_str = exam["scheduled_time"][:10]
                time_str = exam["scheduled_time"][11:16] if len(exam["scheduled_time"]) > 10 else "00:00"
            else:
                date_str = str(exam["scheduled_time"])[:10]
                time_str = str(exam["scheduled_time"])[11:16] if len(str(exam["scheduled_time"])) > 10 else "00:00"
                
            if date_str not in exam_dates:
                exam_dates[date_str] = []
            exam_dates[date_str].append((time_str, exam))
        
        for date in sorted(exam_dates.keys()):
            print(f"\n{date}:")
            daily_exams = sorted(exam_dates[date], key=lambda x: x[0])
            for time_str, exam in daily_exams:
                print(f"  {time_str} - {exam['name']} ({exam.get('room', 'No room')})")
