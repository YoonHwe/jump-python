##5장 연습문제
#1 다음은 Calculator 클래스이다. 위 클래스를 상속하는 UpgradeCalculator를 만들고 값을 뺄 수 있는 minus 메서드를 추가해 보자. 즉 다음과 같이 동작하는 클래스를 만들어야 한다.
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value) # 10에서 7을 뺀 3을 출력

#2 객체변수 value가 100 이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator 클래스를 만들어 보자.
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50) # 50 더하기
cal.add(60) # 60 더하기

print(cal.value) # 100 출력

#3 다음 결과를 예측해 보자.
all([1, 2, abs(-3)-3]) #false

chr(ord('a')) == 'a'

#4 filter와 lambda를 사용하여 리스트 [1, -2, 3, -5, 8, -3]에서 음수를 모두 제거해 보자.
def positive(x):
    return x>0

print(list(filter(positive, [1, -2, 3, -5, 8, -3])))
print(list(filter(lambda x: x > 0, [1, -2, 3, -5, 8, -3])))

#5 234라는 10진수의 16진수는 다음과 같이 구할 수 있다.
#>>> hex(234)
#'0xea'
# 이번에는 반대로 16진수 문자열 0xea를 10진수로 변경해 보자.
int('0xea', 16)