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

# ➜ dodavanje novog kursa svim studentima
for student in students:
    student["courses"]["Databases"] = 9

results = []

passed_count = 0

najveci_prosjek = 0
najmanji_prosjek = 100
best_student = ""
worst_student = ""

# ➜ glavna petlja
for student in students:
    courses = student["courses"]
    average_grade = sum(courses.values()) / len(courses)

    if average_grade >= 6:
        status = "Pass"
        passed_count += 1
    else:
        status = "Fail"

    # spremanje za sortiranje
    results.append((student["name"], average_grade, status))

    # najveći prosjek
    if average_grade > najveci_prosjek:
        najveci_prosjek = average_grade
        best_student = student["name"]

    # najmanji prosjek
    if average_grade < najmanji_prosjek:
        najmanji_prosjek = average_grade
        worst_student = student["name"]

# ➜ sortiranje po prosjeku
results = sorted(results, key=lambda x: x[1], reverse=True)

print("\n--- SORTIRANI STUDENTI ---")
for name, avg, status in results:
    print(f"{name} — average: {avg:.1f} — {status}")

# ➜ najbolji i najlošiji
print("\nNajveci prosjek:", best_student, f"({najveci_prosjek:.1f})")
print("Najmanji prosjek:", worst_student, f"({najmanji_prosjek:.1f})")

# ➜ procenat položenih
percentage_passed = (passed_count / len(students)) * 100
print(f"\nProcenat polozenih studenata: {percentage_passed:.1f}%")