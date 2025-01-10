# append
a = [1, 2, 3]
a.append(4)
print(a)

# insert
a.insert(1, 5)
print(a)

# sort
aa = [1, 4, 3, 2]
aa.sort()
print(aa)

ab = ['a', 'c', 'b']
ab.sort()
print(ab)
ab.sort(reverse=True)
print(ab)

# reverse
# 전체적으로 변환
ac = ['a', 'c', 'b']
ac.reverse()
print(ac)

# index
ad = [1, 2, 3]
print(ad.index(3))

ad = [1, 3, 2, 3, 3]
print(ad.index(3))

# remove
# 첫 번째로 나오는 x를 삭제하는 함수
ae = [1, 2, 3, 1, 2, 3]
ae.remove(3)
print(ae)
ae.remove(3)
print(ae)

# count
# 리스트에 포함된 요소 x의 개수 세기
af = [1, 2, 3, 1]
print(af.count(1))

# extend
# 리스트 확장
ag = [1, 2, 3]
ag.extend([4, 5])
print(ag)
