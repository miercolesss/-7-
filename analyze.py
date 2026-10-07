INPUT_FILE="students.csv"
OUTPUT_FILE="result.txt"
math_sum = 0
english_sum = 0
python_sum = 0
count = 0
best_average = 0
best_student = ""

with open("students.csv") as f :
    next(f)

    for line in f:
        line = line.strip()
        parts = line.split(",")
        name = parts[0]
        m = int(parts[1])
        p = int(parts[2])
        e = int(parts[3])
        math_sum += m
        python_sum += p
        english_sum += e
        count += 1
        avg = (m + p + e) / 3
        if avg > best_average:
            best_average = avg
            best_student = name
math_avg = math_sum / count
english_avg = english_sum / count
python_avg = python_sum / count

result = (
    "Середній бал по класу:\n"
    f"math: {math_avg:.1f}\n"
    f"python: {python_avg:.1f}\n"
    f"english: {english_avg:.1f}\n"
    "\n"
    f"Найкращий студент: {best_student} ({best_average:.1f})"
)
with open("result.txt", "w") as f :
    f.write(result)
print(result)