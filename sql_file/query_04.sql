-- Знайти середній бал на потоці (по всій таблиці оцінок).

SELECT ROUND(AVG(sl.score), 1) AS average_grade
FROM score_log sl