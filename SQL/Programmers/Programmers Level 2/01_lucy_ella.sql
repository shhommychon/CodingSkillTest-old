-- 루시와 엘라 찾기 (String, Date)
-- SELECT, WHERE-IN, ORDER BY
-- https://programmers.co.kr/learn/courses/30/lessons/59046?language=oracle

SELECT animal_id, name, sex_upon_intake
FROM animal_ins
WHERE name IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY animal_id;