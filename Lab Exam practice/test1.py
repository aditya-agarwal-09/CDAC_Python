def main():
    students = [

        {"id": "1", "name": "vignesh","course": "bda","marks": 90.0,"grade": "A"},
        {"id": "2", "name": "Adi","course": "bda","marks": 95.0,"grade": "A"},
        {"id": "3", "name": "souma","course": "Banking","marks": 70.0,"grade": "B"},
        {"id": "4", "name": "max","course": "AI","marks": 45.0,"grade": "f"},
        {"id": "5", "name": "battousai","course": "cyber","marks": 69.0,"grade": "C"}
    ]
    next_id = 6

    def calculate_grade(marks)->str:
        ...
        if marks >= 85.0:
            return 'A'
        elif 85.0 > marks >= 70.0:
            return 'B' 
        elif 70.0 > marks >= 50.0:
            return 'C' 
        elif marks < 50.0:
            return 'F'
        else:
            print("enter valid marks")

    def non_empty_string(prompt: str) -> str:
        while True:
            val = input(prompt).strip()
            if val:
                return val
            print("Error: Please enter string")

    def get_marks() -> float:
        while True:
            val = float(input("Enter the marks: "))
            try:
                if 0.0 < val <100.0:
                    return val
                else:
                    print("Error: please enter valid marks")

            except ValueError:
                print("Error: please enter intergers only")

    while True:
        print("student Menu catalog")
        print('='*42) 
        print("""[1]Enroll students [2]cohort directory
        [3]Query Records [4]Revise evaluation 
        [5]Purge record  [6]Save to jason
        [7]Load from json [8]Terminate""")
        choice = input("print the operation to perform: ")


        if choice == '1':
            print("----ENROLL STUDENT----")
            print('='*62)
            name = non_empty_string("Enter candidate name: ")
            course = non_empty_string("Enter the course: ")
            marks = get_marks()
            grade = calculate_grade(marks)
            new_student = {"id": next_id, "name": name, "course": course, "marks": marks,"grade":grade }
            students.append(new_student)
            print("successfully added")
            next_id += 1

        if choice == '2':
            print("----COHORT DIRECTORY----")
            if not students:
                print("No entries in directory")
            else:
                print(f"{'ID':<10}{'name':<15}{'course':<18}{'marks':<12}{'grade':<8}")
                print('-'*60)
                for s in students:
                    print(f"{s['id']:<10}{s['name']:<15}{s['course']:<18}{s['marks']:<12}{s['grade']:<8}")




main()