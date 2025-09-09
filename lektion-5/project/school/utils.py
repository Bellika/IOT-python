def divide(a, b):
    return a / b

def string_to_int(s):
    return int(s)

def calculate_average(grades):

    if isinstance(grades, dict):
        return sum(grades.values()) / len(grades)
    elif isinstance(grades, list):
        return sum(grades) / len(grades)
    else:
        raise ValueError("has to be list or dict")
    
def print_student_info(name, grades):

    if isinstance(grades, dict):
        grades_str = ', '.join(f"{subject}: {score}" for subject, score in grades.items())
    else:
        grades_str = ', '.join(str(score) for score in grades)
    
    print(f"{name} has grades: {grades_str} (average: {calculate_average(grades):.2f})")