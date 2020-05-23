-- 어린 동물 찾기 (SELECT)
-- WHERE, ORDER BY
-- https://programmers.co.kr/learn/courses/30/lessons/59037?language=oracle

SELECT animal_id, name
FROM animal_ins
WHERE intake_condition <> 'Aged'
ORDER BY animal_id;