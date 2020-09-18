'''
Parameter(파라메터)란?
함수를 호출 할 때 함수로 값을 넘겨줄 때 사용하는 변수. 
'파라메터'라고 읽습니다. 한글로 번역된 말은 '매개변수'입니다. p_message가 파라메터 입니다.
'''


def print_message(p_message):
    print(p_message)


print_message("bye")

'''
Parameter여러개 만들기
parameter를 이용하면 외부에서 여러개의 값을 받을 수 있다.
'''


def print_message_who(p_message, p_who):
    print(p_message, p_who)


print_message_who("hello", "kyeongrok")
