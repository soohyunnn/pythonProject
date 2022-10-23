# 문자열 압축하기
# 문자열을 입력받아 같은 문자가 연속적으로 반복되는 경우 그 반복 횟수를 표시해 문자열을 압축하여 표시
# 먼저 입력 문자열의 문자를 확인하여 동일한 문자가 들어올 경우에는 해당 문자의 숫자 값을 증가시킨다.
# 만약 다른 문자가 들어올 경우에는 해당 문자의 숫자 값을 1로 초기화하는 방법을 사용하여 작성한 코드이다.
def compress_string(s):
    _c = ""
    cnt = 0
    result = ""
    for c in s:
        if c!=_c:
            _c = c
            if cnt: result += str(cnt)
            result += c
            cnt = 1
        else:
            cnt += 1
    if cnt: result += str(cnt)
    return result

print(compress_string("aaabbccccca")) # a3b2c5a1 출력


