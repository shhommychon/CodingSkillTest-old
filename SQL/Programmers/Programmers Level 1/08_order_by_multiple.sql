-- 여러 기준으로 정렬하기 (SELECT)
-- ORDER BY ASC/DESC
-- https://programmers.co.kr/learn/courses/30/lessons/59404?language=oracle

SELECT animal_id, name, datetime
FROM animal_ins
ORDER BY name, datetime DESC;