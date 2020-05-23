-- NULL 처리하기 (IS NULL)
-- NVL
-- https://programmers.co.kr/learn/courses/30/lessons/59410?language=oracle

SELECT animal_type, NVL(name, 'No name'), sex_upon_intake
FROM animal_ins
ORDER BY animal_id;