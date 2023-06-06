[##_Image|kage@biG7k9/btsiuAiwfKe/jQyCVsDwlsbpG6kZJd4xC0/img.jpg|CDM|1.3|{"originWidth":2181,"originHeight":2762,"style":"floatLeft","width":179,"height":227,"link":"https://www.yes24.com/Product/Goods/111408257","isLinkNewWindow":true,"title":"클린코드&amp;#44; 이제 파이썬이다 책 썸네일","filename":"img.jpeg"}_##]

요즘 이 책 시간 날 때마다 보고있는데, 

딕셔너리에 관해서 너무 좋은 내용이 있어서 기록한다.

파이썬으로 api 로직 짜다보면

keyError 가 나는 경우가 있는데, 내가 굉장히 더럽게 코드를 짜서 해결하고 있었더라 하하

여기서 소개하는 딕셔너리 활용법을 이용하면 굉장히 클린하게 해결할 수 있더라고.

#### **get( ), setdefault( )** 

그동안 나는 keyError가 나거나 할 때, 아래와 같은 방식으로 해결을 했다. 

```
orderNo = None if 'orderNo' not in data else data["orderNo"]
```

살짝 자바스크립트의 삼항연산자 느낌 같기도 하고..?

근데 이 책에선 이게 파이썬 답지 않은 코드이자, 악취나는 코드라고 소개하고 있다.

이걸 딕셔너리의 내장함수인 get() 이나 setDefault( )를 이용하면, 정말 깔끔해진다.

**1\. get 사용법**

data.get( key, key에 대응되는 value값 없을 시 기본값 )

```
data = { 'orderNo' : 282828288 }
orderNo = data.get('orderNo', 0)
count = data.get('count', 0)

print(orderNo) // 282828288
print(count) // 0
```

**2\. **setdefault** 사용법**

그러나 아래와 같은 코드에서 또 다시 keyError가 발생한다.

data에 있는 count엔 값 자체가 없기 때문에

data\['count'\] +=10 에서 없는 데이터라 연산이 불가능하기 때문이다. 

```
data = { 'orderNo' : 282828288 }
orderNo = data.get('orderNo', 0)
count = data.get('count', 0)

data['count'] += 10 // 여기서 부터 keyError 발생함
```

이럴 때, setDefault 메소드를 써주는 거다. 

count라는 key가 없을 경우, 0으로 기본값을 설정해주면 key가 존재하지 않아도 error 없이 10을 출력할 수 있게 된다. 

```
data = { 'orderNo' : 282828288 }
orderNo = data.get('orderNo', 0)
count = data.setdefault('count', 0) // count값이 없을 경우 0으로 기본값 설정

data['count'] += 10
print(data['count']) // 10
```

#### **collections.defaultdict**

collections.defaultdict 클래스를 사용하면, keyError를 전부 제거할 수 있다.

기본값에 사용할 데이터 타입을 넘겨 collections.defaultdict( ) 메소드를 호출하면 기본 딕셔너리를 만들 수 있다.

예를 들어 list를 기본 데이터 타입으로 설정하고 싶다면, 아래와 같이 짜주면된다.

```
order = collections.defaultdict(list);
print(type(order)) // <class 'collections.defaultdict'>

order['orderNo'].append('282828')
order['orderNo'].append('101010')

print(order['orderNo']) // [ "282828",  "101010" ]
```

이렇게 하니까 벌써부터 keyError에서부터 자유로워지는 느낌이다.

이제 api 에러로그에, 절대 keyErrorr로그가 찍히지 않을 생각을 하니 넘 행복하다.

#### **switch문 대신 딕셔너리**

아니 나는 파이썬에 switch문 없어서 불만이 많았는데, 이것도 딕셔너리로 해결이 가능했다.

```
if orderNo == 282828
	orderer = 'chillin'
elif orderNo == 101010
	orderer = 'jihan'
elif orderNo == 878787
	orderer = 'kozub'
else
	orderer = 'july'
```

딕셔너리로 해결하기 전엔 아래와 같이 if  ~ elif ~ else 이렇게 해결했는데, 

```
order = {
    282828 : 'chillin',
    101010 : 'jihan',
    878787 : 'kozub'
}
    
orderer = order.get(282828, 'july')
print(orderer) // chillin
```

이렇게 하면, 아주 쉽게 파이썬만의 switch문을 완성할 수 있다.

근데 가독성이 좀 떨어져서 많이는 사용안할지도...?