##2장 연습문제
#1 홍길동 씨의 과목별 점수는 다음과 같다. 홍길동 씨의 평균 점수를 구해 보자.
korean = 80
english = 75
math = 55
(korean+english+math)/3
#2 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법에 대해 말해 보자.
if(13 % 2 == 1):
    print("홀수")
else:
    print("짝수")
#3 홍길동 씨의 주민등록번호는 881120-1068234이다. 홍길동 씨의 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.
private_id = "881120-1068234"
front = private_id[:6]
front
back = private_id[7:]
back
#4 주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 주민등록번호에서 성별을 나타내는 숫자를 출력해 보자.
print(private_id[7])
if(private_id[7] == "1"):
    print("남성")
else:
    print("여성")
#5 다음과 같은 문자열 a:b:c:d가 있다. 문자열의 replace 함수를 사용하여 a#b#c#d로 바꿔서 출력해 보자.
a="a:b:c:d"
print(a.replace(":", "#"))
#6 [1, 3, 5, 4, 2] 리스트를 [5, 4, 3, 2, 1]로 만들어 보자.
b = [1,3,5,4,2]
b.sort()
b.reverse()
b
#7 ['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력해 보자.
c = ['Life', 'is', 'too', 'short']
c[0] + c[1] + c[2] + c[3]
" ".join(c)
#8 (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해 보자.
d = (1,2,3) 
e = (4,)
d = d + e
d
#9 다음과 같은 딕셔너리 a가 있다. 다음 중 오류가 발생하는 경우를 고르고, 그 이유를 설명해 보자.
a = dict()
###a[[1]] = 'ptyhon'###에서 오류 발생
#딕셔너리의 키로는 변하는 값(ex. 리스트)을 사용할 수 없기 때문, [1]은 리스트
#10 딕셔너리 a에서 'B'에 해당되는 값을 추출해 보자.
a = {'A': 90, 'B': 80, 'C': 70}
a['B']
a.pop('B')
a
#11 a 리스트에서 중복 숫자를 제거해 보자.(집합 자료형)
a = [1,1,1,2,2,3,3,3,4,4,5]
a = set(a)
a
#12 파이썬은 다음처럼 동일한 값에 여러 개의 변수를 선언할 수 있다. 다음과 같이 a, b 변수를 선언한 후 a의 두 번째 요솟값을 변경하면 b 값은 어떻게 될까? 그리고 이런 결과가 오는 이유에 대해 설명해 보자.
a = b = [1,2,3]
a[1] = 4
print(b)