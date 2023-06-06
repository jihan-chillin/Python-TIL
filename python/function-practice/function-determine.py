# 문제 1
def triple(x):
    print(x*3);


# triple('x')

# 문제 2
# 태어난 해를 네 자리 숫자로 입력하면, 한국 나이를 반환할 수 있는 함수 korean_age()를 작성해라
from datetime import datetime
today = datetime.today()

def koean_age(year):
    myAge = today.year - year + 1
    print(myAge)
    
koean_age(1996)
