marks = [90, 25, 67, 45, 80]

for number in range(len(marks)): # 5 -> range(5) -> [0, 1, 2, 3, 4]
    if marks[number] < 60:
        continue
    print(f"{number + 1} 학생은 합격입니다")