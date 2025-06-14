import argparse
from exam_manager import ExamManager
from scheduler import ExamScheduler
from conflict_checker import ConflictChecker
from visualizer import ScheduleVisualizer
from storage import save_schedule, load_data

def main():
    parser = argparse.ArgumentParser(description="Automated Exam Scheduler")
    subparsers = parser.add_subparsers(dest='command')

    # Add commands
    add_parser = subparsers.add_parser('add', help='Add new exam')
    add_parser.add_argument('--name', required=True)
    add_parser.add_argument('--students', type=int, required=True)
    
    schedule_parser = subparsers.add_parser('schedule', help='Generate schedule')
    view_parser = subparsers.add_parser('view', help='View current schedule')

    args = parser.parse_args()
    
    # Normalize existing data to handle legacy formats
    ExamManager.normalize_exam_data()
    
    exams, rooms = load_data()
    
    if args.command == 'add':
        ExamManager.add_exam(args.name, args.students)
        print(f"Added exam: {args.name} with {args.students} students")
    elif args.command == 'schedule':
        exam_objects = ExamManager.load_exams()
        schedule = ExamScheduler.generate_schedule(exam_objects, rooms)
        save_schedule(schedule)
        print(f"Generated schedule for {len(schedule)} exams")
    elif args.command == 'view':
        ScheduleVisualizer.display_schedule()
    else:
        exam_objects = ExamManager.load_exams()
        ConflictChecker.check_all_conflicts(exam_objects)

if __name__ == "__main__":
    main()