-- 이름이 없는 동물의 아이디 (IS NULL)
-- ORDER BY
-- https://programmers.co.kr/learn/courses/30/lessons/59039?language=oracle

SELECT animal_id
FROM animal_ins
WHERE name IS NULL
ORDER BY animal_id;