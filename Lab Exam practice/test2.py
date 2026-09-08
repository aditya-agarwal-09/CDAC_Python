import json

# Global state to maintain records in memory
students = [
    {"id": "1", "name": "vignesh","course": "bda","marks": 90.0,"grade": "A"},
    {"id": "2", "name": "Adi","course": "bda","marks": 95.0,"grade": "A"},
    {"id": "3", "name": "souma","course": "Banking","marks": 70.0,"grade": "B"},
    {"id": "4", "name": "max","course": "AI","marks": 45.0,"grade": "f"},
    {"id": "5", "name": "battousai","course": "cyber","marks": 69.0,"grade": "C"}
]

# Module A: Grade Evaluation Helper
def evaluate_grade(marks):
    """Calculates letter grade based on marks standard."""
    if marks >= 85.0:
        return 'A'
    elif marks >= 70.0:
        return 'B'
    elif marks >= 50.0:
        return 'C'
    else:
        return 'F'

# Helper: Auto-increment ID generator
def get_next_id():
    """Returns the next auto-incremented Student ID."""
    if not students:
        return 1
    return max(s['id'] for s in students) + 1

# Module A: Student Enrollment
def enroll_student():
    """Prompts for input, validates fields, and creates a student record."""
    print("\n--- Enroll New Student ---")
    
    # Validate Name
    name = input("Enter Student Name: ").strip()
    while not name:
        print("Name cannot be blank. Please try again.")
        name = input("Enter Student Name: ").strip()

    # Validate Course
    course = input("Enter Course / Module: ").strip()
    while not course:
        print("Course cannot be blank. Please try again.")
        course = input("Enter Course / Module: ").strip()

    # Validate Marks
    while True:
        try:
            marks = float(input("Enter Marks Obtained (0.0 to 100.0): "))
            if 0.0 <= marks <= 100.0:
                break
            else:
                print("Error: Marks must be between 0.0 and 100.0.")
        except ValueError:
            print("Invalid input. Please enter a numerical value for marks.")

    student_id = get_next_id()
    grade = evaluate_grade(marks)

    # Record Dictionary Schema
    record = {
        "id": student_id,
        "name": name,
        "course": course,
        "marks": marks,
        "grade": grade
    }

    students.append(record)
    print(f"Student enrolled successfully! Assigned ID: {student_id}, Grade: {grade}")

# Module B: Reporting & Search Engine
def display_cohort():
    """Prints student records in a structured tabular grid."""
    if not students:
        print("\nCohort directory is currently empty.")
        return

    print("\n" + "=" * 65)
    print(f"{'ID':<5} | {'Name':<20} | {'Course':<18} | {'Marks':<6} | {'Grade':<5}")
    print("=" * 65)
    
    for s in students:
        print(f"{s['id']:<5} | {s['name']:<20} | {s['course']:<18} | {s['marks']:<6.2f} | {s['grade']:<5}")
    print("=" * 65)

def search_records():
    """Performs search by ID (exact) or Name/Course (substring)."""
    if not students:
        print("\nCohort directory is currently empty.")
        return

    print("\nSearch Options: [1] Search by ID | [2] Search by Name/Course")
    choice = input("Select choice (1-2): ").strip()

    results = []
    if choice == '1':
        try:
            search_id = int(input("Enter Student ID: "))
            results = [s for s in students if s['id'] == search_id]
        except ValueError:
            print("Invalid ID format.")
            return
    elif choice == '2':
        query = input("Enter Course Name or Student Name substring: ").strip().lower()
        if query:
            results = [
                s for s in students 
                if query in s['name'].lower() or query in s['course'].lower()
            ]
    else:
        print("Invalid search choice.")
        return

    if results:
        print(f"\nFound {len(results)} matching record(s):")
        for s in results:
            print(f"ID: {s['id']} | Name: {s['name']} | Course: {s['course']} | Marks: {s['marks']} | Grade: {s['grade']}")
    else:
        print("No records found matching your query.")

# Module C: Record Mutation & JSON Synchronization
def revise_evaluation():
    """Allows updating student name, course, or marks and updates grade."""
    if not students:
        print("\nCohort directory is currently empty.")
        return

    try:
        student_id = int(input("\nEnter Student ID to revise: "))
    except ValueError:
        print("Invalid Student ID.")
        return

    student = next((s for s in students if s['id'] == student_id), None)
    if not student:
        print("Student ID not found.")
        return

    print(f"Current Record: Name: {student['name']}, Course: {student['course']}, Marks: {student['marks']}, Grade: {student['grade']}")

    # Prompt optional updates
    new_name = input("Enter new Name (leave blank to keep current): ").strip()
    if new_name:
        student['name'] = new_name

    new_course = input("Enter new Course (leave blank to keep current): ").strip()
    if new_course:
        student['course'] = new_course

    new_marks_str = input("Enter new Marks (leave blank to keep current): ").strip()
    if new_marks_str:
        try:
            new_marks = float(new_marks_str)
            if 0.0 <= new_marks <= 100.0:
                student['marks'] = new_marks
                student['grade'] = evaluate_grade(new_marks)
            else:
                print("Marks must be between 0.0 and 100.0. Marks not updated.")
        except ValueError:
            print("Invalid numeric value. Marks not updated.")

    print("Record revised successfully!")

def purge_record():
    """Purges a student record after user confirmation."""
    if not students:
        print("\nCohort directory is currently empty.")
        return

    try:
        student_id = int(input("\nEnter Student ID to purge: "))
    except ValueError:
        print("Invalid Student ID.")
        return

    student = next((s for s in students if s['id'] == student_id), None)
    if not student:
        print("Student ID not found.")
        return

    print(f"Target Record: ID: {student['id']}, Name: {student['name']}, Course: {student['course']}")
    confirm = input("Are you sure you want to delete this record? (y/n): ").strip().lower()
    
    if confirm == 'y':
        students.remove(student)
        print("Record purged successfully.")
        
    else:
        print("Purge operation cancelled.")

def save_to_json(filename="students.json"):
    """Serializes in-memory records to a formatted JSON file."""
    try:
        with open(filename, 'w') as file:
            json.dump(students, file, indent=4)
        print(f"Data saved successfully to '{filename}'.")
    except Exception as e:
        print(f"Failed to save data: {e}")

def load_from_json(filename="students.json"):
    """Deserializes JSON records from file into memory."""
    global students
    try:
        with open(filename, 'r') as file:
            students = json.load(file)
        print(f"Data loaded successfully from '{filename}'. Total records: {len(students)}")
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with empty/current state.")
    except json.JSONDecodeError:
        print(f"File '{filename}' contains corrupted JSON content. Failed to load.")
    except Exception as e:
        print(f"An unexpected error occurred while loading: {e}")

# Interactive CLI Loop
def main():
    while True:
        print("\n" + "=" * 45)
        print(" STUDENT GRADE MANAGEMENT SYSTEM ")
        print("=" * 45)
        print("[1] Enroll Student")
        print("[2] Cohort Directory")
        print("[3] Query Records")
        print("[4] Revise Evaluation")
        print("[5] Purge Record")
        print("[6] Save to JSON")
        print("[7] Load from JSON")
        print("[8] Terminate")
        print("=" * 45)

        choice = input("Enter choice (1-8): ").strip()

        if choice == '1':
            enroll_student()
        elif choice == '2':
            display_cohort()
        elif choice == '3':
            search_records()
        elif choice == '4':
            revise_evaluation()
        elif choice == '5':
            purge_record()
        elif choice == '6':
            save_to_json()
        elif choice == '7':
            load_from_json()
        elif choice == '8':
            print("Terminating CLI session. Goodbye!")
            break
        else:
            print("Invalid choice! Please select an option between 1 and 8.")

if __name__ == "__main__":
    main()