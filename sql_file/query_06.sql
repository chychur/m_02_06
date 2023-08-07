-- Знайти список студентів у певній групі.

SELECT s.name, s.surname
FROM students s
WHERE s.group_id = 3