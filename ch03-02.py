# chapter03-02
# 파이썬 문자형
# ★문자형 중요★

# 문자열 생성
str1 = "mingyu"
str2 = 'kim, seventeen'
str3 = """jun hui"""
str4 = '''moon, SVT'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))       # 문자열 길이, 자주 쓰임


# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))


# 이스케이프 문자
# I'm a boy

print("I'm a boy")
print('I\'m a boy')
print('I\\m a boy')

print('a \t b')
print('a \n b')
print('a \"\" b')
print()

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)

escape_str2 = 'what\'s good?'
print(escape_str2)


# 탭, 줄바꿈
t_s1 = "click \t start!"
t_s2 = "New line \n check!"

print(t_s1)
print(t_s2)
print()

# Raw string
raw_st1 = r'D:\python\test'

print(raw_st1)
print( )

# 멀티라인 입력
multi_str = \
'''
multi string test 
seventeen
scoups JH Josh
jun hoshi ww wz
mingyu the8 dk
boo ver dino
''' 
# 멀티라인으로 정의 후 다음줄에 쓰고 싶을 땐 \ << 역슬래쉬 붙여줘야함

print(multi_str)
print(  )


# 문자열 연산
str_o1 = "python"
str_o2 = "apple"
str_o3 = "what are you doing?"
str_o4 = "Today! is wonwoo of seventeen birthday!"

print(str_o1 * 4)
print(str_o1 +  str_o2)
print('y' in str_o1)
print('n' in str_o1)
print('P' not in str_o1)
print('P' in str_o1)
print()

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))
print()


# 문자열 함수(upper, isaLnum, startswith, count, endswith, isalpha...)

# 시작글자를 대문자로 바꿔주는 함수
print("Capitalize: ", str_o1.capitalize())

## 마지막에 끝나는 문자가 어떤 것인지 알 수 있는 함수
print("endswith?", str_o2.endswith("e"))

## ★중요★ 내가 원하는 위치로 문자 위치 바꾸기
print("replace", str_o1.replace("on", 'nice'))

## 문자 재정렬
print("sorted: ", sorted(str_o1))

## 단어나 문장을 리스트 형태로 배열하여 분리
print("split: ", str_o4.split('!'))


# 반복(시퀀스)
im_str = "good boy!"
print(dir(im_str))      # __iter__ : 반복할 수 있다!

# 출력
for i in im_str:
    print(i)
print()

# 슬라이싱
str_sl = "very nice"
print(len(str_sl))

# 슬라이싱 연습
print(str_sl[0:3])  # 순서대로 0, 1, 2
print(str_sl[5:])   # = [5:9]
print(str_sl[:len(str_sl)])     # str_sl[:9]
print(str_sl[:len(str_sl)-1])   # str_sl[:8]
print(str_sl[1:7:2])
#          1부터 7까지 2칸씩 띄어서 가져와라
print(str_sl[-3:])
print(str_sl[1:-2])
print(str_sl[::2])
print(str_sl[::-1])
print()
## 음수 : ← / 양수 : → 

# 아스키 코드(or 유니코드)
a = 'z'
print(ord(a))       # 문자 → 아스키코드
print(chr(122))     # 아스키코드 → 문자




