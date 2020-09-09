'''
문자열 재정렬:문제
알파벳 대문자와 숫자 0~9 로만 구성된 문자열이 입력으로 주어짐
이 때 모든 알파벳을 오름 차순을 정렬하여 이어서 출력한 뒤에
그 뒤에 모든 숫자를 더한 값을 이어서 출력함
'''

data = input('문자열을 입력')
result = []
value = 0
# 문자를 하나씩 확인하여
for x in data:
    # 알파벳인 경우 결과를 리스트에 삽입
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''. join(result))
