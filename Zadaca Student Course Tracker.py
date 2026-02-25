students = [
{
        "name": "Milos",
        "courses": {
            "Python": 7,
            "Math": 8,
            "Algorithms": 8
        }
    },
    {
        "name": "Milica",
        "courses": {
            "Python": 7,
            "Math": 6,
            "Algorithms": 5
        }
    },
    {
        "name": "Ognjen",
        "courses": {
            "Python": 10,
            "Math": 9,
            "Algorithms": 8
        }
    }
]
results = []
for student in students:
    course = student["courses"]
    average_grade = sum(course.values())/len(course)
    if average_grade >= 6:
        status = "Pass"
    else:
        status = "Fail"
    print(f"{student['name']} - average: {average_grade:.1f}, status: {status}")










