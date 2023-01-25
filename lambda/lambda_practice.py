# 람다함수
# print((lambda x,y:x+y)(10,20))

# map + 람다
test = list(map(lambda x: x ** 2, range(5)))
# print(test)

#reduce + 람다
from functools import reduce
test2 = reduce(lambda x,y : x+y, [0,1,2,3,4])
# print(test2)

test3 = reduce(lambda x,y : y+x, 'abcde')
# print(test3)

#filter
test4 = list(filter(lambda x: x > 5, range(10))) 
# print(test4)

# 연습 
# 놀이기구 이름을 입력받으면, 이름 - 키 하한 - 키 상한 출력
def read(text):
    ridename, limit = text.split(':')
    
    print('rideName : ', ridename)
    print('limit : ', limit)
    
    cmmin = cmmax = None
    if '~' in limit:
        cmmin, cmmax = map(lambda x: int(x.replace('cm', '')), limit.split('~'))
    elif "이상" in limit:
        cmmin = int(limit.split("cm")[0])

    return ridename, cmmin, cmmax


if __name__ == "__main__":
    ridename, cmmin, cmmax = read(input())
    print("이름:", ridename)
    print("하한:", cmmin)
    print("상한:", cmmax)
