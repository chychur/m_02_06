-- Список курсів, які певному студенту читає певний викладач.

SELECT d.name
FROM disciplines d
JOIN score_log sl ON d.id = sl.discipline_id
WHERE sl.student_id = 1 AND sl.teacher_id =2
GROUP BY d.name