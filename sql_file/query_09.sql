-- Знайти список курсів, які відвідує студент.

SELECT d.name
FROM disciplines d
JOIN score_log sl ON d.id = sl.discipline_id
WHERE sl.student_id = 1
GROUP BY d.name