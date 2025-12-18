def check_progress(marks):
    if marks>=60:
        return True
    else:
        return False
    
def student_progress(subject):
    marks=int(input(f"Enter {subject} marks: "))
    result="PASS" if check_progress(marks) else "FAIL"
    print(f"{subject} RESULT: {result}")

student_progress("physics")
student_progress("Maths")
student_progress("chemistry")