try:
    print(3/0)
except Exception as e:
    print(e)
    print("0으로는 나눌수 없습니다")
else:
    print('예외 없이 성공적으로 실행되었습니다')
finally:
    print("예외처리를 마침니다")
