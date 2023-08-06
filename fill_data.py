from random import randint
import sqlite3

import faker

NUMBER_STUDENTS = 30
NUMBER_GROUPS = 3
NUMBER_TEACHERS = 5
NUMBER_DISCIPLINES = 5
NUMBER_SCORES = 20
VALUE_SCORES = 10


# disciplines -> name, teacher_id
# teachers -> name, surname
# students -> name, surname, group_id
# groups -> name
# score_log -> student_id, teacher_id, discipline_id, score

def generate_fake_data(number_students: int, number_group: int, number_teachers: int, number_scores: int, value_score=VALUE_SCORES) -> tuple:
    students = []
    teachers = []
    disciplines = []
    groups = []
    score_log = []

    name_disciplines = ['Physics', 'Math', 'Cybernetics', 'Hydraulics', 'Philosophy']
    name_groups = ['PY-1', 'MTH-13', 'COR-24']

    fake_data = faker.Faker('en_US')

    for _ in range(number_students):
        students.append((fake_data.first_name(), fake_data.last_name(), randint(1, number_group)))

    for _ in range(number_teachers):
        teachers.append((fake_data.first_name(), fake_data.last_name()))

    for student in range(1, number_students + 1):
        for teacher in range(1, number_teachers + 1):
            for score in range(number_scores):
                r_score = randint(1, value_score)
                result = (student, teacher, teacher, r_score)
                score_log.append(result)

    for discipline in name_disciplines:
        counter = 0
        disciplines.append((discipline, counter + 1))

    for group in name_groups:
        groups.append((group,))

    return groups, students, teachers, disciplines, score_log


def insert_data_to_db(groups, students, teachers, disciplines, score_logg) -> None:
    with sqlite3.connect('db/college.db') as con:
        cur = con.cursor()

        sql_to_groups = '''INSERT INTO groups (name) VALUES (?)'''
        cur.executemany(sql_to_groups, groups)

        sql_to_students = '''INSERT INTO students (name, surname, group_id) VALUES (?, ?, ?)'''
        cur.executemany(sql_to_students, students)

        sql_to_teachers = '''INSERT INTO teachers (name, surname) VALUES (?, ?)'''
        cur.executemany(sql_to_teachers, teachers)

        sql_to_disciplines = '''INSERT INTO disciplines (name, teacher_id) VALUES (?, ?)'''
        cur.executemany(sql_to_disciplines, disciplines)

        sql_to_score_log = '''INSERT INTO score_log (student_id, teacher_id, discipline_id, score) VALUES (?, ?, ?, ?)'''
        cur.executemany(sql_to_score_log, score_logg)

        con.commit()


if __name__ == "__main__":
    groups, students, teachers, disciplines, score_logg = generate_fake_data(NUMBER_STUDENTS, NUMBER_GROUPS, NUMBER_TEACHERS, NUMBER_SCORES)
    insert_data_to_db(groups, students, teachers, disciplines, score_logg)
