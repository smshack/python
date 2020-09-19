# 클래스(Class): 반복되는 불필요한 소스코드를 최소화 하면서
#               현실 세계의 사물을 컴퓨터 프로그래밍 상에서
#               쉽게 표현할 수 있도록 해주는 프로그래밍 기술

# 인스턴스: 클래스로 정의된 객체를 프로그램 상에서 이용할 수 있게 만든 변수

# 클래스의 멤버: 클래스 내부에 포함되는 변수
# 클래스의 함수: 클래스 내부에 포함되는 함수(메소드)

# 상속: 다른 클래스의 멤버 변수와 메소드를 물려 받아 사용하는 기법
# 부모와 자식 관계가 존재함
# 자식 클래스: 부모 클래스를 상속 받은 클래스
# 자식 클래스에서는 부모 클래스의 멤버 변수와 메서드를 사용할 수 있다
# 자식 클래스에 부모 클래스와 같은 함수가 있을 경우 자식에서 정의된 함수를 사용한다

class Car:
    # 클래스의 생성자
    def __init__(self, name, color):
        self.name = name  # 클래스의 멤버
        self.color = color  # 클래스의 멤버

    # 클래스 소멸자
    def __del__(self):
        print(self.name, " 인스턴스 소멸")
        # 클래스의 메소드

    def show_info(self):
        print("이름: ", self.name, "/ 색상: ", self.color)

    # Setter 메소드
    def set_name(self, name):
        self.name = name


car1 = Car("1소나타", "red")
car1.show_info()
car2 = Car("2페라리", "blue")
car2.show_info()
car3 = Car("3아반떼", "black")


print(car1.name, "를 구매했습니다!!")
car1.set_name("4아반떼")
print(car1.name, "로 변경하였습니다")
del car3
