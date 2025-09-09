# ERROR HANDLING
#
#
#

from school import students, print_student_info, calculate_average, divide, string_to_int, safe_execute

print("All students:\n")
for name, grades in students.items():
    print_student_info(name, grades)

students["Eva"] = {"math": 90, "english": 87, "history": 93}

top_student = max(students.items(), key=lambda x: calculate_average(x[1]))
print(f'Top student: {top_student[0]} with average {calculate_average(top_student[1]):.2f}')

students.pop('Bob')
for name, grades in students.items():
    print_student_info(name, grades)

if __name__ == "__main__":
    print("\nScript was run directly!")

# Test safe execute

di = {"a": 1, "b": 2}
li = [10, 20, 30]

# division by zero
safe_execute(divide, 10, 0)

# wrong type
safe_execute(divide, 10, "hello")

# conversion
safe_execute(string_to_int, "abc")