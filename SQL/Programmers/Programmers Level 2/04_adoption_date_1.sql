-- 입양 시각 구하가(1) (GROUP BY)
-- TO_CHAR(), TO_NUMBER()
-- https://programmers.co.kr/learn/courses/30/lessons/59412?language=oracle

SELECT TO_NUMBER(TO_CHAR(datetime, 'HH24')) AS "HOUR", COUNT(*)
FROM animal_outs
WHERE TO_NUMBER(TO_CHAR(datetime, 'HH24')) BETWEEN 9 AND 19
GROUP BY TO_NUMBER(TO_CHAR(datetime, 'HH24'))
ORDER BY TO_NUMBER(TO_CHAR(datetime, 'HH24'));