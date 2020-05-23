-- 고양이와 개는 몇 마리 있을까 (GROUP BY)
-- COUNT()
-- https://programmers.co.kr/learn/courses/30/lessons/59040?language=oracle

SELECT animal_type, COUNT(*)
FROM animal_ins
GROUP BY animal_type
ORDER BY animal_type;