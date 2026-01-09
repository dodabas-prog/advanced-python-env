import json

with open("students.json", "r", encoding="utf-8") as f:
    students = json.load(f)

for s in students:
    grades = s.get("grades", [])
    avg = sum(grades) / len(grades) if grades else 0
    s["average_grade"] = round(avg, 2)

with open("students_updated.json", "w", encoding="utf-8") as f:
    json.dump(students, f, ensure_ascii=False, indent=2)