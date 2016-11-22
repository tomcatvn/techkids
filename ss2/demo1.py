student_list = []
while True:
    prompt = input("lam gi (add, remove, print, exit)")
    if prompt == "add":
        new_student=input("ten? ")
        student_list.append(new_student)
    if prompt == "print":
        print("student", student_list)
    if prompt == "remove":
        position = int(input("vi tri (nhap stt)?"))
        while position >= len(student_list):
            position = int(input("moi nhap lai vi tri"))
        student_list.pop(position-1)
    if prompt == "exit":
        exit_answer = input("exit ? (y/n)")
        if exit_answer.lower(y) == "y":
            break
