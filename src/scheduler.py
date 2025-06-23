from datetime import datetime, timedelta
from itertools import groupby
from operator import attrgetter

class ExamScheduler:
    TIME_SLOTS = [
        ("9:00", "11:00"),
        ("12:00", "14:00"),
        ("15:00", "17:00")
    ]

    @staticmethod
    def generate_schedule(exams, rooms):
        # Sort exams by student count (descending) - larger exams scheduled first
        sorted_exams = sorted(exams, key=lambda x: x.student_count, reverse=True)
        sorted_rooms = sorted(rooms, key=lambda x: x["capacity"], reverse=True)
        
        schedule = []
        current_date = datetime.now().date()
        
        for exam in sorted_exams:
            scheduled = False
            for day_offset in range(14):  # Try scheduling within 2 weeks
                date = current_date + timedelta(days=day_offset)
                # Skip weekends
                if date.weekday() >= 5:
                    continue
                    
                for time_slot in ExamScheduler.TIME_SLOTS:
                    for room in sorted_rooms:
                        if room["capacity"] >= exam.student_count:
                            if not ExamScheduler._has_conflict(date, time_slot, room["name"], schedule):
                                exam.scheduled_time = datetime.strptime(
                                    f"{date} {time_slot[0]}", "%Y-%m-%d %H:%M")
                                exam.room = room["name"]
                                schedule.append(exam)
                                scheduled = True
                                break
                    if scheduled:
                        break
                if scheduled:
                    break
            
            if not scheduled:
                print(f"Warning: Could not schedule exam '{exam.name}' with {exam.student_count} students")
                
        return schedule

    @staticmethod
    def _has_conflict(date, time_slot, room, schedule):
        # Check if room is already booked at this time
        slot_start_time = datetime.strptime(time_slot[0], "%H:%M").time()
        return any(
            e.scheduled_time and
            e.scheduled_time.date() == date and
            e.room == room and
            e.scheduled_time.time() == slot_start_time
            for e in schedule
        )
