# Automated Exam Scheduler

This project is a simple Python-based command-line tool for automatically scheduling exams with conflict detection and room assignment. The system optimizes room allocation based on student count and available time slots while avoiding scheduling conflicts.

## Features added

- Automated Scheduling: Intelligently schedules exams based on student count and room capacity (I have used Priority Scheduling here)
- Conflict Detection: Identifies and reports scheduling conflicts
- Room Management: Automatically assigns appropriate rooms based on capacity requirements
- Weekday Scheduling: Automatically skips weekends for exam scheduling

## Installation

Clone the repository:

```
git clone https://github.com/Mugil13/Automated-Exam-Scheduler.git
cd Automated-Exam-Scheduler
```

## Usage

Adding Exams
```
python main.py add --name "Mathematics" --students 80
python main.py add --name "Physics" --students 45
python main.py add --name "Chemistry" --students 60
```

Generate Schedule
```
python main.py schedule
```

View Schedule
```
python main.py view
```

Run main file for checking conflicts

```
python main.py
```

## Data Files

- exams.json: Stores exam information (name, student count)
- rooms.json: Contains room definitions and capacities
- schedule.json: Generated schedule with assignments

## Contribution

- Fork the repository
- Create a feature branch (git checkout -b feature/new-feature)
- Make your changes
- Commit your changes (git commit -am 'Add new feature')
- Push to the branch (git push origin feature/new-feature)
- Create a Pull Request

