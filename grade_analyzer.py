# Task 1 – Process the Scores
def process_scores(students):
    averages = {}
    for name, scores in students.items():
        avg = sum(scores) / len(scores)
        averages[name] = round(avg, 2)
    return averages

# Task 2 – Classify the Grades
def classify_grades(averages):

    # grading thresholds defined inside function
    grade_A = 90
    grade_B = 75
    grade_C = 60

    classified = {}
    for name, avg in averages.items():
        if avg >= grade_A:
            grade = "A"
        elif avg >= grade_B:
            grade = "B"
        elif avg >= grade_C:
            grade = "C"
        else:
            grade = "F"
        classified[name] = (avg, grade)
    return classified


# Task 3 – Generate the Report
def generate_report(classified, passing_avg=70):
    print("===== Student Grade Report =====")
    passed = 0
    failed = 0
    for name, (avg, grade) in classified.items():
        if avg >= passing_avg:
            status = "PASS"
            passed += 1
        else:
            status = "FAIL"
            failed += 1
        print(f"{name:<10} | Avg: {avg:.2f} | Grade: {grade} | Status: {status}")
    print("================================")
    print(f"Total Students : {len(classified)}")
    print(f"Passed         : {passed}")
    print(f"Failed         : {failed}")
    return passed

# Main Block
if __name__ == "__main__":
    students = {
        "Alice": [85, 90, 84],
        "Bob": [60, 65, 62.5],
        "Clara": [95, 97, 96.75]
    }

    averages = process_scores(students)
    classified = classify_grades(averages)
    generate_report(classified)
