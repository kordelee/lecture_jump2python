# 문자열
# 문자열(string)이란 연속된 문자들의 나열
# 따옴표로 둘러싸여 있으면 모두 문자열
# 큰 따옴표(") 와 작은 따옴표(') 동일하다
a = "Life is too short, You need Python"
b = "a"
c = "123"

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


d = """Life is too short, You need python"""
e = '''Life is too short, You need python'''

print(d)
print(e)

f = "Python's favorite food is perl"
print(f)

g = '"Python is very easy." he says.'
print(g)

h = "\"Python is very easy.\" he says."
print(h)

i = "Life is too short\nYou need python"

print(i)

j = '''
Life is too short
You need python
'''

print(j)

k = """
Life is too short
You need python
"""

print(k)

# 이스케이프 코드를 쓰는 것보다 따옴표 3개를 사용하는 것이 훨씬 깔끔하다.
# 이스케이프(escape) 코드란 프로그래밍할 때 사용할 수 있도록 미리 정의해 둔 ‘문자 조합’을 말한다. 주로 출력물을 보기 좋게 정렬하는 용도로 사용한다.