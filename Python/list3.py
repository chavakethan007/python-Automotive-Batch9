marks=[89,95,82,31,45,67,90,99,26]
pass_marks=[x if x>=60 else "failed" for x in marks]
print(pass_marks)
