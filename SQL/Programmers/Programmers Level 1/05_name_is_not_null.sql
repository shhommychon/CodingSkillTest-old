-- 이름이 있는 동물의 아이디 (IS NULL)
-- ORDER BY
-- https://programmers.co.kr/learn/courses/30/lessons/59407?language=oracle

SELECT animal_id
FROM animal_ins
WHERE name IS NOT NULL
ORDER BY animal_id;