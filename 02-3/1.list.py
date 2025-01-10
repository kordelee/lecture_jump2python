# list 배열
# 리스트 안에는 어떠한 자료형도 포함할 수 있다.
# 리스트명 = [요소1, 요소2, 요소3, ...]
# 인덱스로 각 요소에 접근
# 인덱스는 0 부터 시작 되는 정수
# 인덱스는 -1 부터 시작 되는 정수 (뒤로 부터)


odd = [1, 3, 5, 7, 9]

a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = ["Life", "is", "too", "short"]
e = [1, 2, 'Life', 'is']
f = [1, 2, ['Life', 'is']]
ff = list()

print(b[0])
print(b[-1])

print(f[0])
print(f[2][0])

# 슬라이싱
g = [1, 2, 3, 4, 5]
print(g[0:2]) # 뒤쪽 인덱스는 -1 해준 결과 임
print(g[:2])
print(g[2:])
print(g[2:4])

# 리스트 더하기(+)
aa = [1, 2, 3]
ab = [4, 5, 6]
print(aa + ab)

# 리스트 반복하기(*)
ac = [1, 2, 3]
print(ac * 3)

# 리스트 길이 구하기
ad = [1, 2, 3]
print(len(ad))

# 리스트의 수정
ae = [1, 2, 3]
ae[2] = 4
print(ae)

# 리스트의 삭제 (뒤쪽의 인덱스가 당겨짐)
af = [1, 2, 3]
print(af[1])
del af[1]
print(af[1])

ag = [1, 2, 3, 4, 5]
print(ag[1])
del ag[1:3]
print(ag)
print(ag[1])


