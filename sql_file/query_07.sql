-- Знайти оцінки студентів в окремій групі з певного предмета.

SELECT
    s.name,
    s.surname,
    d.name AS subject_name,
    sl.score
FROM students s
INNER JOIN groups grp ON s.group_id = grp.id
INNER JOIN score_log sl ON s.id = sl.student_id
INNER JOIN disciplines d ON sl.discipline_id = d.id
WHERE grp.id = 1 AND d.id = 2;
