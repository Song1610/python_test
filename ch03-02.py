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
