from pathlib import Path

print(Path.cwd())
for f in Path("week02").glob("*.py"):
    print(f)
Path("week03/data/raw").mkdir(parents = True, exist_ok= True)
Path("week03/data/processed").mkdir(parents = True, exist_ok= True)

print(Path("data/raw").exists())

students = [
    {
        "name": "张三",
        "age": 20,
        "scores": [85, 92, 78, 96, 88],
        "city": "北京"
    },
    {
        "name": "李四",
        "age": 21,
        "scores": [90, 87, 93, 85, 91],
        "city": "上海"
    },
    {
        "name": "王五",
        "age": 19,
        "scores": [78, 82, 85, 79, 88],
        "city": "广州"
    },
    {
        "name": "赵六",
        "age": 22,
        "scores": [95, 89, 92, 94, 90],
        "city": "深圳"
    },
    {
        "name": "孙七",
        "age": 20,
        "scores": [82, 76, 88, 84, 80],
        "city": "杭州"
    },
    {
        "name": "周八",
        "age": 23,
        "scores": [88, 91, 85, 87, 93],
        "city": "成都"
    }
]
import json

# Path("data/raw/students.json").mkdir(parents = True, exist_ok=True)
with open("data/raw/students.json", "w", encoding = "utf-8") as f:
    json.dump(students, f, ensure_ascii = False, indent = 2)
with open("data/raw/students.json", "r", encoding = "utf-8") as f:
    students_info = json.load(f)
print(type(students_info) == type(students))

def average(student: dict) -> float:
    scores = student["scores"]
    return sum(scores)/len(scores)

for student in students:
    student["avg_score"] = average(student)
with open("data/processed/students_with_avg.json", "w", encoding = "utf-8") as f:
    json.dump(student, f, ensure_ascii=False, indent = 2)
print(Path("data/raw/students.json").resolve())     # resolve实例方法，不是类方法
print(Path("data/raw/students_with_avg.json").resolve())