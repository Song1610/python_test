# 230604_Chpapter02_01
# 파이썬 완전기초
# prtint 사용법

# 기본출력
print('python start!')
print("python start!")
print('''python start!''')  # 잘 사용하진 않음
print("""python start!""")  # 잘 사용하진 않음
print()


# separator
print('P','Y','T','H','O','N', sep='')
print('010','4064','9746', sep='-')
print('python', 'google.com', sep='@')
print()


# end
print('welcome to', end=' ')
print('IT News', end=' ')
print('web site')
print()


# file
import sys
print('Learn python', file=sys.stdout)
print()


# format 사용(d,s,f)
# d: 정수(3) / s: 문자열'python' / f: 실수 2.1324
print('%s %s' %('ming','gyu'))
print('{} {}'.format('ming','gyu'))
print('{1} {0}'.format('ming','gyu'))
print()


# %s
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:$>10}'.format('nice'))     # 공백 채우기
print('{:^10}'.format('nice'))      # 중앙정렬

print('%5s' %('kimningyu'))
print('%.5s' %('kimningyu'))            # 문자 절삭 .5 에 맞춰서 5글자만 표시해줌
print('{:10.5}'.format('kimningyu'))    # 총 10글자 중 5글자만 나오게 해라
print()


# %d
print('%d %d' %(1,2))
print('{} {}'.format('m0','9'))

print('%4d' %(46))
print('{:4d}'.format(46))       # 정수일 때는 '' 붙여줘야함
print()


# %f
print('%1.8f' % (9747.2341231423423))       # 소수점 뒤에 .8자리까지 나오게 해줘
print('{:f}'.format(97.472341231423423))

print('%06.2f' %(4.06610349189230))
print('{:06.2f}'.format(4.06610349189230))

print()