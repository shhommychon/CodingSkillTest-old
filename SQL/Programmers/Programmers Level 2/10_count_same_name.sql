-- 동명 동물 수 찾기 (GROUP BY)
-- GROUP BY - HAVING
-- https://programmers.co.kr/learn/courses/30/lessons/59041?language=oracle

SELECT name, COUNT(*)
FROM animal_ins
GROUP BY name
HAVING COUNT(name) > 1
ORDER BY name;