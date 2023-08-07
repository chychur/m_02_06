-- Знайти 5 студентів із найбільшим середнім балом з усіх предметів.

SELECT s.name, s.surname, g.name AS group_num, AVG(sc.score) AS average_grade
FROM students s, groups g
JOIN score_log sc ON s.id = sc.student_id
GROUP BY s.name
ORDER BY average_grade DESC
LIMIT 5;