# map과 lambda를 사용하여 [1, 2, 3, 4] 라는 리스트의 각 요솟값에 3이 곱해진 리스트 [3, 6, 9, 12]를 만들어 보자.
# 입력에 항상 3을 곱하여 돌려 주는 lambda 함수를 다음과 같이 만들고 map과 조합하여 실행한다.
result = list(map(lambda x:x*3, [1,2,3,4,5]))
print(result)


