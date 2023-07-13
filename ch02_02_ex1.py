# 230604_Chpapter02_02_ex1
# 파이썬 완전기초
# prtint 사용법
# 파이썬 3가지 print formatting

### 3가지 format Practices

x = 406
y = 100
text = 970406
n = 'mingyu'

# 출력 1
ex1 = 'n = %s, s = %s, sum=%d' % (n, text, (x+y))
print(ex1)


# 출력 2
ex2 = ex1 = 'n = {n}, s = {s}, sum={sum}'.format(n=n, s=text, sum=x+y)
print(ex2)

# 출력 3
ex3 = f'n = {n}, s = {text}, sum={x+y}'
print(ex3)

# 출력 3-1
print(f'n = {n}, s = {text}, sum={x+y}')



# 구분기호
m = 100000000
print(f'm : {m:,}')
print(f'{m:,}')

print()
print()


# 정렬
# ^ : 가운데 / < : 왼쪽 / > : 오른쪽

t = 20
print(f"t : {t:10}")
print(f"t center : {t:^10}")
print(f"t left : {t:<10}")
print(f"t right : {t:>10}")

print()
print()

print(f"t center : {t:-^10}")
print(f"t left : {t:=<10}")
print(f"t right : {t:.>10}")