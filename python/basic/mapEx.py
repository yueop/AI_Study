def convert_to_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
    
scores = [88, 92, 78, 60, 75, 95]
grades = list(map(convert_to_grade, scores))
print(grades)

def myFunc(x):
    if x < 18:
        return False
    else:
        return True
    
ages = [5, 12, 17, 18, 24, 32]
age_over = list(filter(myFunc, ages))
print(age_over)