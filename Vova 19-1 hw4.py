mentors = ["Аблай", "Камиля", "Адахан"]

while True:

    while len(mentors) <= 4:
        mentor = input("выберите mentors: ").title()
        if len(mentor) < 15:
            mentors.append(mentor)
            print(mentors)
        else:
            print("No")

    mentor_old = input("Choose old mentor: ").title()
    if mentor_old not in mentors:
        print("Not in list")
        mentors_tupple = tuple(mentors)
        print(mentors_tupple)
        break

    else:
        mentors.remove(mentor_old)

    mentor_new = input("Choose new mentor: ").title()
    if len(mentor_new) < 15:
        mentors.append(mentor_new)
        print(mentors)
    else:
        print("None")

    mentors_name = input("Введите имя: ")
    if mentors_name in mentors:
        mentors.remove(mentors_name)
        print(mentors)
    else:
        print("Not in list")






