# 230611_Chpapter02_02
# 파이썬 완전 기초
# 파이썬 변수

# 기본선언
n = 700
print(n)
print(type(n))      # 타입을 알려줌 <class 'int'>  → type: 정수형
print()


# 동시선언
x = y = z = 700
print(x, y, z)
print()


# 선언
var = 406

# 재선언
var = "change value"

# 출력
print(var)              # 1차 선언 값은 미출력, 2차 선언값 "change value" 가 출력
print(type(var))
print()


# Object References
# 변수 값 할당상태일 때
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# ex1)
print(300)
print(int(300))
print()

# ex2)
# n -> 406
n = 406

print(n, type(n))
print()


m = n
# m = 406 = n
print(m, n)
print(type(m), type(n))
print()


m = 400
print(m, n)
print(type(m), type(n))
print()


# id(identity) 확인: 객체의 고유값 확인
m = 800
n = 655

print(id(m))        # 오브젝트의 고유값 출력
print(id(n))
print(id(m) == id(n))
print()

# 같은 오브젝트 참조
m = 1997
n = 1997

print(id(m))        # 오브젝트의 고유값 출력
print(id(n))
print(id(m) == id(n))
print()


# 다양한 변수 선언
# Camel case : numberOfCollegeGraduates -> Method 선언
## 처음에 소문자 그 다음에 대문자를 나열하는 것

# Pascal Case : NumberOfCollegeGraduates -> Class 선언
## 첫 시작글자: 대문자

# Snake case : number_of_college_graduates -> 변수 선언할 때 사용


# 허용하는 변수선언
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8
1age= 9
print(age, Age, aGe, AGE, a_g_e, _age, age_, _AGE_, 1age)


# 예약어는 변수명으로 불가능 / 예약어: 파이썬에서 이미 쓰고 있는 거
"""
False def if raise
None del import return
True elif in try
and else is while
as except lambda with
assert finally nonlocal yield
break for not
class from or
continue global pass
"""