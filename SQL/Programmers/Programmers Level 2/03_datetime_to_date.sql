-- DATETIME에서 DATE로 형 변환 (String, Date)
-- to_char()
-- https://programmers.co.kr/learn/courses/30/lessons/59414?language=oracle

SELECT
    animal_id,
    name,
    TO_CHAR(datetime, 'YYYY-MM-DD')
FROM animal_ins
ORDER BY animal_id;