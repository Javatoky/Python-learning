for i in range(1, 6):
    line = [f"{i*j:>4}" for j in range(1, 6) ]
    print("".join(line))

pi = 3.141592653589793
print(f"{pi:.2f}")
print(f"{pi:.6f}")
print(f"{pi:.2%}")
print(f"{pi:.2e}")

students = [
    ("Alice", 92, 88, 95),
    ("Bob", 78, 82, 75),
    ("Charlie", 85, 90, 88),
]
separator = f"{'='*(10+8*4)}"
print(separator)
print(f"{'姓名':>10}{'语文':>8}{'英语':>8}{'英语':>8}{'平均':>8}")
print(separator)
for name, *score in students:
    line = [f"{s:>8}" for s in score]
    avg = sum(score) / len(score)
    print(f"{name:>10}" + "".join(line) + f"{avg:>8.2f}")
print(separator)