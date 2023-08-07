-- Знайти середній бал, який ставить певний викладач зі своїх предметів.

SELECT
    t.name,
    t.surname,
    d.name AS subject_name,
    ROUND(AVG(sl.score), 1) AS average_grade
FROM teachers t
INNER JOIN score_log sl ON t.id = sl.teacher_id
INNER JOIN disciplines d ON sl.discipline_id = d.id
GROUP BY t.name