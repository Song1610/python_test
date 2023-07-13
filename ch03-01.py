# chapter03-01
# 숫자형

# 파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
"""

# 데이터 타입
str1 = "SVT"
bool = True
str2 = 'mingyu'
float_m = 10.0    # 10 =/= 10.0
int_m = 7
list = [str1, str2]
dict = {
    "name" : "min9"
    , "version" : 2.0
}

tuple = (7, 8, 9)
# tuple = 7, 8, 9
# 도 사용 가능
set = {4, 0, 6}

# 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_m))
print(type(int_m))
print(type(list))
print(type(dict))
print(type(tuple))
print(type(set))


# 숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x, y) or x ** y → x^y
ex) 2 ** 3 or pow(2, 3) = 8
"""

# 정수 선언
i = 77
i2 = -14
big_int = 3904810931298205694819082309127581931223412893719823128379123

# 정수 출력
print(i)
print(i2)
print(big_int)
print()

# 실수 선언
f = 0.999
f2 = 4.063291
f3 = -3.9
f4 = 3 / 9

# 실수 출력
print(f)
print(f2)
print(f3)
print(f4)
print()

# 연산 실습
i1 = 39
i2 = 9890
big_int1 = 32948091802937810847398187903
big_int2 = 20348112312904823095823842304819273102498
f1 = 1.997
f2 = 4.065


# +
print(">>>> +")
print("i1 + i2 = ", i1 + i2)
print("f1 + f2 = ", f1 + f2)
print("big_int1 + big_int2 = ", big_int1 + big_int2)
print()

# -
print(">>>> -")
print("i1 - i2 = ", i1 - i2)
print("f1 - f2 = ", f1 - f2)
print("big_int1 - big_int2 = ", big_int1 - big_int2)
print()

# *
print(">>>> *")
print("i1 * i2 = ", i1 * i2)
print("f1 * f2 = ", f1 * f2)
print("big_int1 * big_int2 = ", big_int1 * big_int2)
print()

# /
print(">>>> /")
print("i1 / i2 = ", i1 / i2)
print("f1 / f2 = ", f1 / f2)
print("big_int1 / big_int2 = ", big_int1 / big_int2)
print()


# 형 변환 실습
a = 3.
b = 6
c = .7
d = 12.7

# 타입 출력
print(type(a), type(b), type(c), type(d))

# 형변환
print(int(a))
print(float(b))
print(int(c))
print(int(d))
print(int(True))    # Ture : 1, False : 0
print(int(False))
print(float(False))
###### ▲까지 알아두면 좋음 / ▼ 는 잘 안쓰임 ######
print(complex(3))
print(complex('3'))     # 문자형 -> 숫자형 바꾼 뒤 형변환
print(complex(False))
print()

# 수치연산 함수
print(abs(-7))  # 절대값을 돌려준다. 출력결과 값: 7

x, y = divmod(100, 8)       # 몫과 나머지를 구해줌 // 많이 쓰임
print(x,y)

print(pow(5,3), 5 ** 3)


# 외부모듈
import math

print(math.pi)
print(math.ceil(5.1))       # x 이상의 수 중에서 가장 작은 정수 찾아주기
