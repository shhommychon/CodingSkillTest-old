### 프로그래머스 Level1
### 신규 아이디 추천 | 2021 KAKAO BLIND RECRUITMENT
### https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3

class FirstException(Exception):
    pass

class SecondException(Exception):
    pass

class ThirdException(Exception):
    pass

class FourthException(Exception):
    pass

class FifthException(Exception):
    pass

class SixthException(Exception):
    pass

class SeventhException(Exception):
    pass

def solution(new_id):
    # step 1.
    try:
        new_id = new_id.lower()
    except Exception as e:
        raise FirstException(str(e))
    
    # step 2.
    try:
        new_id = ''.join([ 
            char for char in new_id \
            if char in "abcdefghijklmnopqrstuvwzyx0123456789-_." 
        ])
    except Exception as e:
        raise SecondException(str(e))
    
    # step 3.
    try:
        while '..' in new_id:
            new_id = new_id.replace("..", '.')
    except Exception as e:
        raise ThirdException(str(e))
    
    # step 4.
    try:
        if len(new_id) > 0 and new_id[0] == '.':
            temp_list = list(new_id)
            temp_list.pop(0)
            new_id = ''.join(temp_list)
        if len(new_id) > 0 and new_id[-1] == '.':
            temp_list = list(new_id)
            temp_list.pop()
            new_id = ''.join(temp_list)
    except Exception as e:
        raise FourthException(str(e))
    
    # step 5.
    try:
        if len(new_id) == 0:
            new_id = 'a'
    except Exception as e:
        raise FifthException(str(e))
    
    # step 6.
    try:
        if len(new_id) >= 16:
            new_id = new_id[:15]
            if new_id[-1] == '.':
                new_id = new_id[:-1]
    except Exception as e:
        raise SixthException(str(e))
    
    # step 7.
    try:
        if len(new_id) <= 2:
            end_char = new_id[-1]
            while len(new_id) < 3:
                new_id += end_char
    except Exception as e:
        raise SeventhException(str(e))
            
    return new_id