### 소에아 4단계
### 5550번 나는 개구리로소이다

T = int(myinput())

CROAK = "croak"
def is_valid_croak(chr1, chr2):
    assert chr2 in CROAK, chr2
    return  CROAK[CROAK.index(chr2)-1] == chr1

for test_case in range(1, T + 1):
    frog_croaks = myinput()
    frogs = [[]]; answer = len(frogs)

    for chr in frog_croaks:
        if answer == -1: break # skip rest

        frog_appended = False
        if chr == CROAK[0]: # 'c'
            for frog in frogs:
                if len(frog) == 0:
                    frog.append(chr)
                    frog_appended = True; break
            if not frog_appended:
                frogs.append([chr]); frog_appended = True # new frog
        elif chr == CROAK[-1]: # 'k'
            for frog in frogs:
                if frog and is_valid_croak(frog[-1], chr):
                    frog.clear()
                    frog_appended = True; break
            if not frog_appended:
                answer = -1; break # not frog croak
        elif chr in CROAK:
            for frog in frogs:
                if frog and is_valid_croak(frog[-1], chr):
                    frog.append(chr)
                    frog_appended = True; break
            if not frog_appended:
                answer = -1; break # not frog croak
        else:
            pass
    
    # frogs에 남아 있는 울음소리가 있는지 확인
    for frog in frogs:
        if frog:
            answer = -1; break
    
    answer = len(frogs) if answer != -1 else -1
    print(f"#{test_case} {answer}")