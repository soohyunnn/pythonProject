# DashInsert 함수
# 숫자로 구성된 문자열을 입력받은 뒤 문자열 안에서 홀수가 연속되면 두 수 사이에 -를 추가하고, 짝수가 연속되면 *를 추가하는 기능을 갖고 있다.

data = "4546793"
numbers = list(map(int, data))
result = []

for i, num in enumerate(numbers):
    result.append(str(num))
    if i < len(numbers)-1:          # 다음 수가 있다면
        is_idd = num % 2 == 1       # 현재 수가 홀수
        is_next_odd = numbers[i+1] %2 == 1  # 다음 수가 홀수
        if is_idd and is_next_odd:      # 연속 홀수
            result.append("-")
        elif not is_idd and not is_next_odd:    # 연속 짝수
            result.append("*")

print("".join(result))


