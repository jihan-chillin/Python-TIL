students = [ 'jihan', 'chillin', 'kozub']
grades = [ 2, 1, 4 ]

print('students[1] : ', students[1])
print('length : ', len(students))


print(min(grades))
print(max(grades))


import statistics # 통계 모듈
print('grades의 평균',statistics.mean(grades))

import random # 랜덤 모듈
print('random.choice(students) : ', random.choice(students)) # 랜덤뽑기 

