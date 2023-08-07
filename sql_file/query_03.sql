-- Знайти середній бал у групах з певного предмета.

SELECT g.name, ROUND(AVG(sl.score), 1) AS average_grade
FROM groups g, disciplines d
JOIN students s on g.id = s.group_id
JOIN score_log sl ON s.id = sl.student_id
WHERE sl.discipline_id = 2 -- 'Math'
GROUP BY g.name

