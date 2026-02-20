# 평점
grade_dict = { 
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}

credit_sum = 0 # 총 학점
score_sum = 0 # 학점*평점의 총합
for _ in range(20):
    obj, credit, grade = input().split()

    if(grade != 'P'):
        score = grade_dict[grade] 
        credit = float(credit)
        score_sum = score_sum + (score * credit) # 학점*평점 합
        credit_sum += credit # 학점 합

major_avg = score_sum / credit_sum
print(major_avg)
