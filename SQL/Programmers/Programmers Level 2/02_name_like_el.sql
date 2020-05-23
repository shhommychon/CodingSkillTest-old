-- 이름에 el이 들어가는 동물 찾기 (String, Date)
-- SELECT, WHERE-LIKE, ORDER BY, upper()
-- https://programmers.co.kr/learn/courses/30/lessons/59047?language=oracle

SELECT animal_id, name
FROM animal_ins
WHERE animal_type = 'Dog'
AND upper(name) LIKE '%EL%'
ORDER BY name;