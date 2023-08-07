-- Знайти студента із найвищим середнім балом з певного предмета.

SELECT s.name, s.surname, g.name AS group_name, AVG(sc.score) AS average_grade
FROM students s, groups g
JOIN score_log sc ON s.id = sc.student_id
WHERE sc.discipline_id = 2 --'Math'
GROUP BY s.name
ORDER BY average_grade DESC
LIMIT 1;