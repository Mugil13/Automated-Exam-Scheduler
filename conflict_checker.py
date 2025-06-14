from collections import defaultdict
from datetime import timedelta

class ConflictChecker:
    @staticmethod
    def check_all_conflicts(exams):
        room_bookings = defaultdict(list)
        time_conflicts = []
        
        for exam in exams:
            if exam.scheduled_time:
                room_bookings[exam.room].append((exam.scheduled_time, exam.name))
        
        for room, bookings in room_bookings.items():
            sorted_bookings = sorted(bookings, key=lambda x: x[0])
            for i in range(len(sorted_bookings) - 1):
                current_end = sorted_bookings[i][0] + timedelta(hours=2)
                next_start = sorted_bookings[i+1][0]
                
                if next_start < current_end:
                    time_conflicts.append(
                        f"Room {room} has overlapping exams: "
                        f"{sorted_bookings[i][1]} at {sorted_bookings[i][0]} and "
                        f"{sorted_bookings[i+1][1]} at {sorted_bookings[i+1][0]}"
                    )
        
        if time_conflicts:
            print("\nCONFLICTS DETECTED:")
            for conflict in time_conflicts:
                print(f"! {conflict}")
        else:
            print("No scheduling conflicts detected")
