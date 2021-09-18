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

#6 map과 lambda를 사용하여 [1, 2, 3, 4] 리스트의 각 요솟값에 3이 곱해진 리스트 [3, 6, 9, 12]를 만들어 보자
list(map(lambda x:x*3, [1,2,3,4]))

#7 다음 리스트의 최댓값과 최솟값의 합을 구해 보자.
list = [-8, 2, 7, 5, -3, 5, 0, 1]
max = max(list)
min = min(list)
print(max+min)

#8 5.666666666666667을 소수점 4자리까지만 반올림하여 표시해 보자.
round(5.666666666666667, 4)

#9 다음처럼 sys모듈의 argv를 사용하여 명령 행 입력값 모두를 차례로 더해 준다.
import sys
numbers = sys.argv[1:] # 파일 이름을 제외한 명령 행의 모든 입력
result = 0
for number in numbers:
    result += int(number)
print(result)

#10 os 모듈을 사용하여 다음과 같이 동작하도록 코드를 작성해 보자 1.C:\doit 디렉터리로 이동한다. / 2. dir 명령을 실행하고 그 결과를 변수에 담는다. / 3. dir 명령의 결과를 출력한다.

#11 glob 모듈을 사용하여 C:\doit 디렉터리의 파일 중 확장자가 .py인 파일만 출력하는 프로그램을 작성해 보자.
import glob
glob.glob("c:/doit/*.py")

#12 time 모듈을 사용하여 현재 날짜와 시간을 다음과 같은 형식으로 출력해 보자.
import time 
time.strftime("%Y/%m/%d %H:%M:%S") # %Y:년, %m:월, %d:일, %H:시, %M:분, %S:초

#13 random 모듈을 사용하여 로또 번호(1~45 사이의 숫자 6개)를 생성해 보자.
import random
result = []
while len(result) < 6:
    num = random.randint(1, 45)   # 1부터 45까지의 난수 발생
    if num not in result:
        result.append(num)
print(result)